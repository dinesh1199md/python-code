
{
    "product01": {
      "after_deployment": {
        "test": {
          "owner": "EY",
          "repo": "exec",
          "file": "config.yml",
          "after_environment": True,
          "wait_for_deploy": False,
          "fail_on_error": False,
          "extra details":["xml","json"]
        }
      }
    }
  }
  
  
def read(l):
    finallist=[]
    
    with open(json.file,"r") as file:
        lines=fles.readlines()
        
        for line in lines:
            if l in line:  
                out=line.split(":")
                finallist.append(out[1])
                
    return finallist      
    
    
print(read("owner"))
    
    