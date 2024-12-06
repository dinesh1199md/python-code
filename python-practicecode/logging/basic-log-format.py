import logging
logging.basicConfig(filename="loggingcheck.log",filemode="a",format="%(asctime)s %(message)s")
logg=logging.getLogger()
logg.setLevel(logging.INFO)

def div(a,b):
        try: 
            c=a/b
            print(f"the div value: {c}")
            logg.info(f"the div value: {c}")
        except Exception as e:
            # print(e)   
            logging.exception(e) 
        finally:
            logg.info("div is done")            

if __name__=="__main__":
    logg.info("script is started")
    div(100,0)
    # logging.info("function call done")    
    