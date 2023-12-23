import replicate
import os 

os.environ["REPLICATE_API_TOKEN"] = "LL-7V3u02Tx2rlG9ktrLeLAI8JsmJyPaDxRLfKCkvLrVYvCSdsiint2ivcr4S40kWUt"

output = replicate.run(
    
  "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
  input={
    "prompt": "Can you write a poem about open source machine learning?"
  }
)
print(output)