from pydantic import BaseModel
from sekoia_automation.module import Module
from glimps_custom_modules.models import GlimpsCustomModuleConfiguration


class Response(BaseModel):
    text: str


class GlimpsCustomModule(Module):
    configuration: GlimpsCustomModuleConfiguration

