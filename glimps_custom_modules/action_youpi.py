from pydantic import BaseModel
from sekoia_automation.action import Action


class Response(BaseModel):
    text: str


class Arguments(BaseModel):
    pass


class Youpi(Action):
    results_model = Response

    def run(self, arguments: Arguments) -> Response:
        return Response(text="youpi")
