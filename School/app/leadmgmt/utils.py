from fastapi.responses import JSONResponse
from fastapi import status


def jsonresponse(reasonCode,status,reasonText,responseObject,totalRecords,responseListObject):
    json={
        "reasonCode":reasonCode,
        "status":status,
        "reasonText":reasonText,
        "responseObject":responseObject,
        "totalRecords":totalRecords,
        "responseListObject":responseListObject
    }
    return json


def leadpayloadcheckschool(addSchool):
    id = addSchool.id
    designation = addSchool.designation
    name = addSchool.name
    phone_number = addSchool.phone_number

    if id=="" or id==None:
         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content= jsonresponse('400','fail','data cannot be empty','','',''))
    
    if designation=="" or designation==None:
         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content= jsonresponse('400','fail','data cannot be empty','','',''))

    if name=="" or name==None:
         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content= jsonresponse('400','fail','data cannot be empty','','',''))

    if phone_number=="" or phone_number==None:
         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content= jsonresponse('400','fail','data cannot be empty','','',''))

    return JSONResponse(status_code=status.HTTP_200_OK,content=jsonresponse("400","fail","Payload Valid","","",""))

def leadpayloadcheckupdate(updateschool):
    designation = updateschool.designation
    name = updateschool.name
    phone_number = updateschool.phone_number

    if designation=="" or designation==None:
         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content= jsonresponse('400','fail','data cannot be empty','','',''))

    if name=="" or name==None:
         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content= jsonresponse('400','fail','data cannot be empty','','',''))

    if phone_number=="" or phone_number==None:
         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content= jsonresponse('400','fail','data cannot be empty','','',''))

    return JSONResponse(status_code=status.HTTP_200_OK,content=jsonresponse("400","fail","Payload Valid","","",""))


def leadpayloadcheck(addClass):
    id=addClass.id
    techers_id =addClass.techers_id
    name_of_student = addClass.name_of_student

    if id=="" or id==None:
         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content= jsonresponse('400','fail','data cannot be empty','','',''))
    
    if techers_id=="" or techers_id==None:
         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content= jsonresponse('400','fail','data cannot be empty','','',''))

    if name_of_student=="" or name_of_student==None:
         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content= jsonresponse('400','fail','data cannot be empty','','',''))

    return JSONResponse(status_code=status.HTTP_200_OK,content=jsonresponse("400","fail","Payload Valid","","",""))