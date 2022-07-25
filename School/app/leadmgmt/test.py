from queue import Empty
from tabnanny import check
from fastapi import HTTPException, status
from sqlalchemy import null
from app.config.dbconfig import sessionLocal
from app.config import model,app_config
import psycopg2.extras
from app.leadmgmt.utils import *
from fastapi import APIRouter
from app.config import schemas

post_route = APIRouter()

db=sessionLocal()

conn = psycopg2.connect('postgresql://postgres:postgres@localhost/School_db')


@post_route.post("/schools/add")
def addSchool(school:schemas.School):
    db_data=db.query(model.School).filter(model.School.name==school.name).first()

    if db_data is not None:
        raise HTTPException(status_code=400,detail="Item already exists")

    leadpayloadresponse=leadpayloadcheckschool(school)
    if leadpayloadresponse.status_code==status.HTTP_400_BAD_REQUEST:
        return leadpayloadresponse

    new_data={}
    new_data=model.School(
        id=school.id,
        designation=school.designation,
        name=school.name,
        phone_number=school.phone_number
        
    )
    db.add(new_data)
    data={}
    data['id']=new_data.id
    data['designation']=new_data.designation
    data['name']=new_data.name
    data['phone_number']=new_data.phone_number
    
    db.commit()
    
    return jsonresponse("200","success","School employee information Added successfully ",data,"1","1")


@post_route.post("/class/add")
async def addClass(classes:schemas.Classes):
    leadpayloadresponse=leadpayloadcheck(classes)
    if leadpayloadresponse.status_code==status.HTTP_400_BAD_REQUEST:
        return leadpayloadresponse

    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute('''select designation from school2
                    WHERE id = %s''' ,[classes.techers_id,])
    des_teacher = cursor.fetchone()

    if(des_teacher[0]!="teacher"):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not a valid teacher")

    cursor.execute('''select designation from school2
                    WHERE name = %s''' ,[classes.name_of_student,])
    des_student = cursor.fetchone()

    db_count=db.query(model.Classes).count()
    
    if(des_student[0]!= "student"):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Only student can Enter in class")
    if(db_count!=0):
        cursor.execute('''select techers_id from classes2
                    ''' )
        id_teacher = cursor.fetchone()
        if(id_teacher[0]!=None and id_teacher[0]!=classes.techers_id):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Only one teacher will be there {id_teacher}")

    data = db.query(model.Classes).all()
    if(len(data)==5):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Can't Take any student")

    # print(des_teacher[0])

    new_data=model.Classes(
        id=classes.id,
        techers_id=classes.techers_id,
        name_of_student=classes.name_of_student,
        
    )


    db.add(new_data)
    db.commit()
    
    data={}
    data['id']=new_data.id
    data['teacher_id']=new_data.techers_id
    data['name_of_student']=new_data.name_of_student

    return jsonresponse("200","success","Class employee information Added successfully ",data,"1","1")

@post_route.delete("/class/delete")
def deleteClass(delete:schemas.getPayloadClass):
    item_to_delete=db.query(model.Classes).filter(model.Classes.id==delete.id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(item_to_delete)
    db.commit()
    
    data={}
    data['id']=item_to_delete.id
    data['teacher_id']=item_to_delete.techers_id
    data['name_of_student']=item_to_delete.name_of_student

    return jsonresponse("200","success","Class employee information Deleted successfully ",data,"1","1")


@post_route.post("/schools/get")
def getSchool(get:schemas.getPayloadSchool):
    counts=0
    checkid=get.id
    if checkid=="" or checkid==None:
        new_data = db.query(model.School).all() 
        counts=len(new_data)

    else:
        try:                
            checkid = int(checkid)
        except Exception as e:
            return jsonresponse('400','fail','School Id is not valid','','','')
        new_data=db.query(model.School).filter(model.School.id==get.id).first()   
        counts=1

  

    
    return jsonresponse("200","success","School information Fetched successfully ","",counts,new_data)

@post_route.post("/class/get")
def getClass(get:schemas.getPayloadSchool):
    checkid=get.id
    counts=0
    if checkid=="" or checkid==None:
        new_data = db.query(model.Classes).all() 
        counts=len(new_data)

    else:
        try:                
            checkid = int(checkid)
        except Exception as e:
            return jsonresponse('400','fail','School Id is not valid','','','')
        new_data=db.query(model.Classes).filter(model.Classes.id==get.id).first() 
        counts=1

    
    
    return jsonresponse("200","success","School information Fetched successfully ","",counts,new_data)

@post_route.put("/schools/update")
def updateSchool(updateschool:schemas.School):
    item_to_update=db.query(model.School).filter(model.School.id==updateschool.id).first()

    leadpayloadresponse=leadpayloadcheckupdate(updateschool)
    if leadpayloadresponse.status_code==status.HTTP_400_BAD_REQUEST:
        return leadpayloadresponse

    item_to_update.designation=updateschool.designation
    item_to_update.name=updateschool.name
    item_to_update.phone_number=updateschool.phone_number

    db.commit()

    data={}
    data['id']=item_to_update.id
    data['designation']=item_to_update.designation
    data['name']=item_to_update.name
    data['phone_number']=item_to_update.phone_number

    return jsonresponse("200","success","School employee information Updated successfully ",data,"1","1")

@post_route.delete("/schools/delete")
def deleteSchool(delete:schemas.getPayloadClass):
    item_to_delete=db.query(model.School).filter(model.School.id==delete.id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(item_to_delete)
    db.commit()

    data={}
    data['id']=item_to_delete.id
    data['designation']=item_to_delete.designation
    data['name']=item_to_delete.name
    data['phone_number']=item_to_delete.phone_number

    return jsonresponse("200","success","School employee information Deleted successfully ",data,"1","1")