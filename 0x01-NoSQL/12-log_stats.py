#!/usr/bin/env python3
'''log parsing fro database'''
import pymongo 

if __name__ == "__main__":
  client = pymongo.MongoClient("mongodb://localhost:27017")
  db = client.logs
  logs = db.nginx.count_documents({})

  results = db.nginx.aggregate(
      [{"$group": {"_id": "$method", "total": {"$count": {}}}}]
  )
  get_status = db.nginx.count_documents({"method": "GET", "path": "/status"})

  dic = {}

  for res in results:
      dic[res["_id"]] = res["total"]

  print(f"{logs} logs")
  print("Methods:")
  print(f'    method GET: {dic.get("GET", 0)}')
  print(f'    method POST: {dic.get("POST", 0)}')
  print(f'    method PUT: {dic.get("PUT", 0)}')
  print(f'    method PATCH: {dic.get("PATCH", 0)}')
  print(f'    method DELETE: {dic.get("DELETE", 0)}')
  print(f"{get_status} status check")
