
class ExtractModelChildren:
    """
    Extracts linked Children of a Model class

    Parameter: Model Class
    """

    def __init__(self, model_class):
        self.model_class = model_class

    def __extract_item(self, instance, item_list: list):
        """
        Recursively call and check if there is any child available.
        """
        if not isinstance(instance, type(None)):
            db_objects = self.model_class.objects.filter(parent_id=instance)
            if db_objects.exists():
                for ct in db_objects:
                    item_list.append(ct)
                    self.__extract_item(ct, item_list)
                return item_list
        return item_list

    def extract_raw_children(self, model_instance):
        """
        Returns Raw Children

        Parameter: Model Instance
        """
        return self.__extract_item(model_instance, [])


    def extract_serialized_children(self, model_instance, model_serializer):
        """
        Returns Serialized Children

        Parameters: Model Instance, Model Serializer
        """
        children = [model_instance] + self.extract_raw_children(model_instance) 
        return  [model_serializer(child).data for child in children]
