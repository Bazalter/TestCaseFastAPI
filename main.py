from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Any
import models, schemas
from database import get_db, engine


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/ads/", response_model=List[schemas.Ad])
def read_ads(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    ads = db.query(models.Ad).offset(skip).limit(limit).all()
    return ads


@app.get("/ads/{ad_id}", response_model=schemas.Ad)
def read_ad(ad_id: int, db: Session = Depends(get_db)):
    ad = db.query(models.Ad).filter(models.Ad.id == ad_id).first()
    if ad is None:
        raise HTTPException(status_code=404, detail="Ad not found")
    return ad


@app.post("/ads/", response_model=schemas.Ad)
def create_ad(ad: schemas.AdCreate, db: Session = Depends(get_db)):
    db_ad = models.Ad(**ad.dict())
    db.add(db_ad)
    db.commit()
    db.refresh(db_ad)
    return db_ad


@app.post("/ads/few/", response_model=List[schemas.Ad])
def create_ads(ads: schemas.AdCreateList, db: Session = Depends(get_db)):
    db_ads = [models.Ad(**ad.dict()) for ad in ads.ads]
    db.bulk_save_objects(db_ads)
    db.commit()
    return db_ads
