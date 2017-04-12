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

    def __init__(self, voc_image_path='VOCdevkit/VOC2012/JPEGImages',
                 voc_image_set_path='VOCdevkit/VOC2012/ImageSets/Main/trainval.txt',
                 voc_annon_path='VOCdevkit/VOC2012/Annotations'):
        self.current_work_dir = os.getcwd()
        self.voc_image_path = os.path.join(self.current_work_dir, voc_image_path)
        self.voc_image_set_path = os.path.join(self.current_work_dir, voc_image_set_path)
        self.voc_annon_path = os.path.join(self.current_work_dir, voc_annon_path)
        self._annotation_line_list = [] # a list of annotations, each annontation is dict
        self._parse_from_voc() # parse all the data

    @property
    def annotation_line_list(self):
        return self._annotation_line_list

    def get_annotation_dataframe(self):
        """
        Returns a dataframe with the parsed pascal voc data. When an image has several bbox annotations, the resulting dataframe\
        has a line for each.

        Example:

        voc_parser.get_annotation_dataframe()

|   | class_name  | height  | img  | img_full_path  | width  | xmax  | xmin  | ymax  | ymin  |
|---|---|---|---|---|---|---|---|---|---|
| 0  | tvmonitor  | 375.0  | 2008_000002  | /home/user/Personal/playground/voc/VOCdevkit/V...  | 500.0  | 448   | 34 | 293  | 11  |
| 1  | train  | 333.0  | 2008_000003  | /home/user/Personal/playground/voc/VOCdevkit/V...  | 500.0  | 500  | 46  | 333  | 11  |
| 2  | person  | 333.0  | 2008_000003  | /home/user/Personal/playground/voc/VOCdevkit/V...  | 500.0  | 83  | 62  | 243  | 190  |

        """
        return pd.DataFrame(self.annotation_line_list)

    def get_annotation_dataframe_compact(self):
        """
        Returns a dataframe only two columns, img_full_path and annon. The annon column contain all the bbox and class for\
        each image. It has the following for each image:

        (((xmin1, ymin1, xmax1, ymax1), class_name1), ((xmin2, ymin2, xmax2, ymax2), class_name2) )

        Example:

        voc_parser.get_annotation_dataframe_compact()

|   | img_full_path  | annon  |
|---|---|---|
| 0  | /home/user/Personal/playground/voc/VOCdevkit/V...  | (((34, 11, 448, 293), tvmonitor),)  |
| 1  | /home/user/Personal/playground/voc/VOCdevkit/V...  | (((46, 11, 500, 333), train), ((62, 190, 83, 2...  |


        """        
        temp_df = pd.DataFrame(self.annotation_line_list)
        # make a list with the annotations for each bbox (each row of the fata frame)
        temp_df['annon'] = list(zip(list(zip(temp_df['xmin'], temp_df['ymin'], temp_df['xmax'], temp_df['ymax'])), temp_df['class_name']))
        # group the df based on im_full_path
        grouped = temp_df.groupby(['img_full_path'])
        # create tuples of the grouped rows columns
        df_serie = grouped['annon'].aggregate(lambda x: tuple(x))
        return df_serie.to_frame()


    def _parse_from_voc(self):
        # get all the files names from the voc_imageset_text_path
        filenames_list = helpers.get_file_lines(self.voc_image_set_path)

        #for each filename from the image set we need to get the annotations
        for filename in filenames_list:
            # get the path of the annotation file
            annotation_file = self._get_img_detection_filepath(self.voc_annon_path, filename)
            # tree of the xml
            tree = ElementTree.parse(annotation_file)
            # get the root element
            root_node = tree.getroot()
            # get file name
            img_filename = root_node.find('filename').text
            img_full_path = self._get_img_filepath(img_filename)
            # get the size of the image from the annotation xml file
            width, height = self._get_img_size(root_node)

            #get the the list of all object trees from the annotation xml
            object_tree_list = root_node.findall('object')

            #for each object tree
            for object_annotation in object_tree_list:
                # create a dictionary with all the information
                # {img,img_full_path,width,height,class_name,xmin,ymin,xmax,ymax}
                row_dictionary = {}

                class_name = self._get_annotation_classname(object_annotation)
                obj_bbox = object_annotation.find('bndbox')
                xmin, ymin, xmax, ymax = self._get_annotation_bbox(obj_bbox)

                # now that we have all the information from an annotation bbox
                # create a dict to be inserted in the final result
                row_dictionary.update({'filename': filename,
                                       'full_path': img_full_path,
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

    def _get_img_filepath(self, image):
        return os.path.join(self.voc_image_path, image)
        
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
