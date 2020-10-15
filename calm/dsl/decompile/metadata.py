from calm.dsl.decompile.render import render_template
from calm.dsl.builtins import MetadataType
from calm.dsl.decompile.ref_dependency import update_package_name


def render_metadata_template(cls):

    if not isinstance(cls, MetadataType):
        raise TypeError("{} is not of type {}".format(cls, MetadataType))

    cls_data = cls.get_dict()
    user_attrs = {}

    if cls_data.get("categories"):
        user_attrs["categories"] = cls_data["categories"]

    # NOTE: Project and Owner info is not provided by calm export_file api yet.
    # When available add their rendered_text to user_attrs and modify jinja template accordingly

    # NOTE: Name of class is constant i.e. BpMetadata

    # If metadata is not available, return empty string
    if not user_attrs:
        return ""

    text = render_template("metadata.py.jinja2", obj=user_attrs)

    return text.strip()
