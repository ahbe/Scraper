import uvicorn
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from facebook_scraper import get_posts
import pandas as pd
from sqlalchemy import create_engine




app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class Request(BaseModel):
    page: str
    number_pages: int = 3
    
@app.post('/facebook')
def predict(req:Request):
    
    page = req.page # name of the  page requested
    number_pages = req.number_pages # number of pages to scrape
    
    data_columns = ['Date_post','Post','Likes','Comments','Shares'] # columns names to scrape
    data =  pd.DataFrame(columns = data_columns) # creating dataframe to save data
    
    for post in get_posts(page, pages=number_pages):
        dict = {'Date_post': post['time'].strftime('%Y-%m-%d %H:%M:%S') , 'Text': post['text'], 'Likes': post['likes'],'Comments': post['comments'],'Shares': post['shares'] }
        # temp dict to fetch specific data
        data = data.append(dict, ignore_index = True)
        # add fetch data to dataframe
    
    table_name = "Data" # table and file name
    
    engine = create_engine('postgresql://postgres:postgres@host.docker.internal:5432/facebook_db') # create postgres engine
    data.to_sql(table_name, engine) # writes to postgres
    
    # conn = sq.connect('{}.sqlite'.format(table_name)) # creates file
    # data.to_sql(table_name, conn, if_exists='replace', index=False) # writes to file
    
    # conn.close() # close connection
    
    res = f"done with scrapping {page} from facebook with a total of {number_pages} pages scraped." # respose to return 
    
    return Response(json.dumps(res),media_type='application/json')



if __name__ == '__main__':
    uvicorn.run("scraper:app", host="0.0.0.0", port=1053)