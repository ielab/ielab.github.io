---
redirect_from: /agask-agent
authors: [hang-li, bevan-koopman, ahmed-mourad, guido-zuccon]
title: "AgAsk: A Conversational Search Agent for Answering Agricultural Questions"
venue: The 16th ACM International Conference on Web Search And Data Mining
pdf: /publications/pdfs/wsdm2023-agask-demo.pdf
year: 2023
links:
 - url: https://youtu.be/uItp9LsC1UE
   name: Demo on Youtube 
---
---

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/uItp9LsC1UE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Installation

Macaw is running with Python 3.8, so make sure you have it installed. If you don't have `setuptools`, run `sudo pip3 install setuptools`. The mentioned installation commands can be executed on Ubuntu. You can use the same or similar commands on other Linux distribution.

#### Step 1: Installing MongoDB Server
Macaw uses MongoDB for storing and retrieving user interactions (conversations). To install MongoDB server, run the following command:
```
sudo apt-get install mongodb-server-core
```

#### Step 2: Installing Pyserini
[Pyserini](https://github.com/castorini/pyserini) is an open-source search engine for information retrieval research, we replaced the original Indri retrieval engine with Pyserini for easier development.

To install Pyserini:
```
pip3 install pyserini==0.14.0
```

Install pytorch and transformers:
```
pip3 install torch==1.6.0+cpu torchvision==0.7.0+cpu transformers==4.21.1
```

#### Step 3: Installing Macaw
First, clone the Macaw fork from our github repo:
```
git clone https://github.com/ielab/macaw.git
cd macaw
sudo pip3 install -r requirements.txt
sudo python3 setup.py install
```

#### Step 4: Create Telegram bot
We refer the readers to [How to Create a Telegram Bot](https://learn.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-telegram?view=azure-bot-service-4.0) page for detailed instructions.

#### Step 5: Change the Configurations
We need to make some changes to the configs to run our version of Macaw:
```
cd macaw/macaw/
sudo vim live_main.py
```
In this file, you need to modify the `bot_token` in the `interface_params`, which you need to get by creating a bot in Telegram (Step 4). In `retrieval_params` you need to change the `pyserini_index` parameter to point to the location that stores your pyserini index file. and same for `tilde-v2_index`.

The `results_requested` and `retrieval_requested`, you can change them depend on your needs.

## Running Macaw
We run our version of Macaw as in live version, first of all, we need to start the MongoDB server:
```
sudo mongod
```
Note that this command uses the default database directory (`/data/db`) for storing the data. You may need to create 
this directory if you haven't. You can also use other locations using the `--dbpath` argument. 
```
python3 live_main.py
```
Run the above command to start the Macaw server.

To use the retrieval mode, issue your question with `Search: ` as a prepend, if want to use QA mode, issue your question with `QA: ` as a prepend. If no prepend found, Macaw will run in QA mode in default.

In retrieval mode, Macaw will reply with a list of retrieved passages, in QA mode, Macaw will generate a specific answer to the question asked.
