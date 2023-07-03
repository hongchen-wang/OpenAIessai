import logging
import openai
import azure.functions as func

# { "model": "text-ada-001", "prompt": "tell me a commercial slogan for a software company", "max_tokens": 100, "temperature": 0}


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # give OpenAI our secrte_key to authenticate
    openai.api_key = secret_key

    # get variables form the HTTP request body
    req_body = req.get_json()

    # call the OpenAI API
    output = openai.Completion.create(
        model = req_body['model'],
        prompt = req_body['prompt'],
        max_tokens = req_body['max_tokens'],
        temperature = req_body['temperature']
    )

    # format the response
    output_text = output['choices'][0]['text']

    # echo the response
    return func.HttpResponse(output_text, status_code=200)