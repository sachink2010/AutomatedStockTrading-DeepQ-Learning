Please find the project inside Zip file  that contain the multiple folders 
1.	State : in this folder you will find the state.py file 
2.	Agent :inside this folder you will get  Agent.py file 
3.	Trading.ipynb file that contains functionality:

3.1	Data pre-processing
3.2	Agent is trained with 51 Episode. Input here are following parameters: 
- Stock1_name: this is first stock name, which is Apple - aapl.us
- Stock2_name: this is second stock name, which is Amazon - amzn.us
- episode_count: This is number of episodes which agent till train on
- Start_balance: This is the initial starting cash, which is $ 10,000
- Training: This is number of records used for trading i.e. number of days on each episode of training will run
- Test: This is number of days on which test run will be executed 
 
3.3	Evaluate and final program that predict the  total portfolio value for one episode 

4. Models are saved in model directory

To execute the program, you would need to run the Trading.IPynb file with input as stated above and then look at the result

5. There are other files: Testing- Google n Walmart.ipynb and Testing-IBM n GE.ipynb. These can be used to test the model generated in Trading.ipynb and stored in Models directory




References
1.	MACHINE LEARNING FOR TRADING: GORDON RITTER: https://cims.nyu.edu/~ritter/ritter2017machine.pdf
2.	Financial Trading as a Game: A Deep Reinforcement Learning Approach: Huang, Chien-Yi
https://arxiv.org/pdf/1807.02787.pdf
3.	Convergence of Q-learning: a simple proof: Francisco S. Melo:
http://users.isr.ist.utl.pt/~mtjspaan/readingGroup/ProofQlearning.pdf

4.	https://medium.com/@chinmaya.mishra1/deep-dive-in-to-reinforcement-learning-10fa30b418f9
5.	David Silver’s lectures about deep reinforcement learning

