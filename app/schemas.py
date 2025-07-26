from pydantic import BaseModel

class WheelSpecFields(BaseModel):
    treadDiameterNew: str
    lastShopIssueSize: str
    condemningDia: str
    wheelGauge: str
    variationSameAxle: str
    variationSameBogie: str
    variationSameCoach: str
    wheelProfile: str
    intermediateWWP: str
    bearingSeatDiameter: str
    rollerBearingOuterDia: str
    rollerBearingBoreDia: str
    rollerBearingWidth: str
    axleBoxHousingBoreDia: str
    wheelDiscWidth: str

class WheelSpecCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: str
    fields: WheelSpecFields

class WheelSpecResponse(WheelSpecCreate):
    class Config:
        orm_mode = True