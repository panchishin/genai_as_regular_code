# README

Thanks for looking at these examples of how GEN AI can be used in everyday code using API calls.

There are 7 examples that use simple calls that help with regular everyday tasks.

They all use llm_service.py which is simply a REST call to Ollama

You can install Ollama locally from https://ollama.ai

Once installed you can load a wide variety of language models.

For these examples use the following zsh command that loads llama2:13b-chat-q6_K which at the time of writing is a fairly powerful model that runs fairly fast on local hardward.  You'll need about 20G of free RAM to run it, but that should be very doable on our hardware.

`ollama run llama2:13b-chat-q6_K`

Once you run that on the command line the python files should work fine