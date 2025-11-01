from database import SessionLocal
from fastapi import APIRouter
from sqlmodel import func, desc
from sqlalchemy import select, outerjoin
from models import SSSOOTweets, SSSOOTweetMedia
from pydantic import BaseModel

router = APIRouter()

@router.get("/sssootweets")
def get_topsssootweets():
    with SessionLocal() as session:
        sssooTweetsModel = SSSOOTweets
        sssooTweetsMediaModel = SSSOOTweetMedia
        
        statement = select (
            sssooTweetsModel.ID,
            sssooTweetsModel.TweetID,
            sssooTweetsModel.TweetText,
            sssooTweetsModel.TweetLongText,
            sssooTweetsMediaModel.MediaKey,
            sssooTweetsMediaModel.MediaUrl            
        ).select_from(outerjoin(sssooTweetsModel, sssooTweetsMediaModel, sssooTweetsModel.ID==sssooTweetsMediaModel.SSSOOTableTweetId))
            # sssooTweetsModel).join(target=sssooTweetsMediaModel, onclause=sssooTweetsModel.ID==sssooTweetsMediaModel.SSSOOTableTweetId, full=False)
        
        sssooTweets = session.execute(statement).mappings().all()

        return sssooTweets
    
