from . import helpers
from xml.etree import ElementTree
import pandas as pd
import os

class VocAnnotationsParser(object):
    """ Visual Object Classes Challenge 2012 Annotation Data parsing functionality.

        This class is intended to be used for the "Detenction competition", please refer to:\
        http://host.robots.ox.ac.uk/pascal/VOC/voc2012/#introduction

        The dataset can be downloaded from: http://host.robots.ox.ac.uk/pascal/VOC/voc2012/#devkit

        The main functionality is simple, it receives one of the image sets text files from the\
        "VOCdevkit/VOC2012/ImageSets", parse all the lines and for each image it reads the file\
        in "VOCdevkit/VOC2012/Annotations" and obtain annotation data. It returns one Pandas\
        Dataframe with all the annotation data from each image in the rows, each row has the\
        following fiels:

        filename, full_file_path, width, height, class_name, xmin, ymin, xmax, ymax

    """

    def __init__(self):
        self._annotation_line_list = [] # a list of annotations, each annontation is dict

    @property
    def annotation_line_list(self):
        return self._annotation_line_list

    def get_annotation_dataframe(self):
        return pd.DataFrame(self.annotation_line_list)

    def parse_from_voc(self, voc_imageset_text_path,\
                                     voc_annotations_path):
        # get all the files names from the voc_imageset_text_path
        filenames_list = helpers.get_file_lines(voc_imageset_text_path)

        #for each filename from the image set we need to get the annotations
        for filename in filenames_list:
            # get the path of the annotation file
            annotation_file = self._get_img_detection_filepath(voc_annotations_path, filename)
            # tree of the xml
            tree = ElementTree.parse(annotation_file)
            # get the root element
            root_node = tree.getroot()
            # get the size of the image from the annotation xml file
            width, height = self._get_img_size(root_node)

            #get the the list of all object trees from the annotation xml
            object_tree_list = root_node.findall('object')

            #for each object tree
            for object_annotation in object_tree_list:
                # create a dictionary with all the information {img,img_full_path,width,height,class_name,xmin,ymin,xmax,ymax}
                row_dictionary = {} 

                class_name = self._get_annotation_classname(object_annotation)
                obj_bbox = object_annotation.find('bndbox')
                xmin, ymin, xmax, ymax = self._get_annotation_bbox(obj_bbox)

                #now that we have all the information from an annotation bbox create a dict to be inserted in the final result
                row_dictionary.update({'filename': filename,
                                       'full_path': annotation_file,
                                       'width': width,
                                       'height': height,
                                       'class_name': class_name,
                                       'xmin': xmin,
                                       'ymin': ymin,
                                       'xmax': xmax,
                                       'ymax': ymax})
                self._annotation_line_list.append(row_dictionary)

    def _get_img_detection_filepath(self, voc_annotations_path, img_name):
        return os.path.join(voc_annotations_path, img_name + '.xml')

    def _get_img_size(self, root_node):
        size_tree = root_node.find('size')
        width = float(size_tree.find('width').text)
        height = float(size_tree.find('height').text)
        return (width, height)
    
    def _get_annotation_classname(self, object_annotation):
        return object_annotation.find('name').text
    
    def _get_annotation_bbox(self, bbox_node):
        xmin = int(round(float(bbox_node.find('xmin').text)))
        ymin = int(round(float(bbox_node.find('ymin').text)))
        xmax = int(round(float(bbox_node.find('xmax').text)))
        ymax = int(round(float(bbox_node.find('ymax').text)))
        return (xmin, ymin, xmax, ymax)