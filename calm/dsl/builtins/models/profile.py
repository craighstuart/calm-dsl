from .entity import EntityType, Entity
from .validator import PropertyValidator


# Profile


class ProfileType(EntityType):
    __schema_name__ = "Profile"
    __openapi_type__ = "app_profile"

    def get_task_target(cls):
        return

    @classmethod
    def pre_decompile(mcls, cdict, context, prefix=""):
        cdict = super().pre_decompile(cdict, context, prefix=prefix)

        if "__name__" in cdict:
            cdict["__name__"] = "{}{}".format(prefix, cdict["__name__"])

        return cdict

    def compile(cls):
        cdict = super().compile()
        # description attribute in profile gives bp launch error: https://jira.nutanix.com/browse/CALM-19380
        cdict.pop("description", None)
        return cdict


class ProfileValidator(PropertyValidator, openapi_type="app_profile"):
    __default__ = None
    __kind__ = ProfileType


def profile(**kwargs):
    name = kwargs.get("name", None)
    bases = (Entity,)
    return ProfileType(name, bases, kwargs)


Profile = profile()
