# Bedrock PDF Summary

This code is based on this original [blog post](https://medium.com/@naresh.kancharla/pdf-summarizer-using-llm-108881921189), where Naresh provides guidance on how to use ChatGPT API to synthesize a pdf.

In case you run into OpenAI's token limits, and/or prefer to use AWS offering, this code allows you to use Claude from Amazon Bedrock.

My [blog post](https://compellingcloud.substack.com/p/summarizing-pdf-and-estimating-token) where I explain the background and highlights.

## Disclaimers:
- Not production ready
- This is a personal educational project not affiliated with any company

## Use
0. Install and run virtual env
```
pip install virtualenv
virtualenv venv
source venv/bin/activate

```
1. Configure your AWS account locally by running
```
aws configure --profile <profile-name>
```
2. Rename example.env to .env, and update it with your profile name
3. Execute
```
pip install -r requirements.txt
python app.py
```
4. Go to http://127.0.0.1:7860/