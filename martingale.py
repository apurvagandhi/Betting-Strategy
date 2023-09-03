""""""  		  	   		  		 		  		  		    	 		 		   		 		  
"""Assess a betting strategy.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		  		 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  		 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		  		 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		  		 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		  		 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 		  		  		    	 		 		   		 		  
or edited.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		  		 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		  		 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   	
Project Link: https://lucylabs.gatech.edu/ml4t/fall2022/project-1/	  		 		  		  		    	 		 		   		 		  
Student Name: Apurva Gandhi	  	   		  		 		  		  		    	 		 		   		 		  
GT User ID: agandhi301		  	   		  		 		  		  		    	 		 		   		 		  
GT ID: 903862828	  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import numpy as np  
import matplotlib.pyplot as plt		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def author():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    return "agandhi301"  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def gtid():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: int	  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    return 903862828  	   		  		 		  		  		    	 		 		   		 		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def get_spin_result(win_prob):  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    :param win_prob: The probability of winning  		  	   		  		 		  		  		    	 		 		   		 		  
    :type win_prob: float  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The result of the spin.  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: bool  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    result = False  		  	   		  		 		  		  		    	 		 		   		 		  
    if np.random.random() <= win_prob:  		  	   		  		 		  		  		    	 		 		   		 		  
        result = True  		  	   		  		 		  		  		    	 		 		   		 		  
    return result  		 
   	  		 		  		  		    	 		 		   		 		  
def gambling_simulation(win_prob, bankRoll):
    episode_winnings = 0
    episode_array = np.full(1001, 80)
    episode_array[0] = 0
    spin_count = 0
    
    while episode_winnings < 80:
        won = False
        bet_amount = 1
        while not won:
            if spin_count >= 1001:
                return episode_array
            episode_array[spin_count] = episode_winnings
            spin_count = spin_count + 1
            won = get_spin_result(win_prob)
            if won == True:
                episode_winnings = episode_winnings + bet_amount
            else:
                episode_winnings = episode_winnings - bet_amount
                bet_amount = bet_amount * 2	
                if bankRoll:
                    if episode_winnings <= -256:
                        episode_array[spin_count:] = -256
                        return episode_array
                    if episode_winnings - bet_amount < -256:
                        bet_amount = episode_winnings + 256

    return episode_array
   		  		 		  		  		    	 		 		   		 		  
def test_code():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Method to test your code  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    win_prob = 9/19  # set appropriately to the probability of a win  		  	   		  		 		  		  		    	 		 		   		 		  
    np.random.seed(gtid())  # do this only once  		  	   		  		 		  		  		    	 		 		   		 		  
    perform_experiment_1_get_figure1(win_prob)
    perform_experiment_1_get_figure2_and_figure3(win_prob)
    perform_experiment_2_get_figure4_and_figure5(win_prob)

def perform_experiment_1_get_figure1(win_prob):
    #Figure 1 plotting and calculation
    plt.axis([0, 300, -256, 100])
    plt.xlabel("Round")
    plt.ylabel("Winnings")
    plt.title("10 Episode Spin Rolls with Unlimited Bets")
    plt.grid(True)
 
    for i in range (10): 
        episode = gambling_simulation(win_prob, False) 
        plt.plot(episode)
    plt.legend(labels = range(1,11)) 		  		 		  		  		    	 		 		   		 		  
    plt.savefig("fig1.png")  
    plt.clf()
    		  		 		  		  		    	 		 		   		 		  
def perform_experiment_1_get_figure2_and_figure3(win_prob):
    # Generating data
    figure2_and_figure3_episodes = np.empty((1000,1001))
    for i in range (1000):
        episode = gambling_simulation(win_prob, False) 
        figure2_and_figure3_episodes[i] = episode

    #Figure 2 Calcualtion 
    mean = np.mean(figure2_and_figure3_episodes, axis = 0)
    standard_deviation = np.std(figure2_and_figure3_episodes, axis = 0)
    mean_plus_standard_deviation = mean + standard_deviation
    mean_minus_standard_deviation = mean - standard_deviation
    # Figure 2 Plotting
    plt.axis([0, 300, -256, 100])
    plt.xlabel("Round")
    plt.ylabel("Winnings")
    plt.title("Mean of Each Spin with Unlimited Bets")
    plt.grid(True)
    plt.plot(mean, label = "mean")
    plt.plot(mean_plus_standard_deviation, label = "mean+")
    plt.plot(mean_minus_standard_deviation, label = "mean-")
    plt.legend()
    plt.savefig("fig2.png")
    plt.clf()
    
    #Figure 3 Calculation
    median = np.median(figure2_and_figure3_episodes, axis = 0)
    standard_deviation = np.std(figure2_and_figure3_episodes, axis = 0)
    median_plus_standard_deviation = median + standard_deviation
    median_minus_standard_deviation = median - standard_deviation
    #Figure 3 Plotting
    plt.axis([0, 300, -256, 100])
    plt.xlabel("Round")
    plt.ylabel("Winnings")
    plt.title("Median of Each Spin with Unlimited Bets")
    plt.grid(True)
    plt.plot(median, label = "median")
    plt.plot(median_plus_standard_deviation, label = "median+")
    plt.plot(median_minus_standard_deviation, label = "median-")
    plt.legend()
    plt.savefig("fig3.png")
    plt.clf()

def perform_experiment_2_get_figure4_and_figure5(win_prob):
    # Generating data
    figure4_and_figure5_episodes = np.empty((1000,1001))
    for i in range (1000):
        episode = gambling_simulation(win_prob, True)
        # print(episode) 
        figure4_and_figure5_episodes[i] = episode
    
    #Figure 4 Calcualtion 
    mean = np.mean(figure4_and_figure5_episodes, axis = 0)
    standard_deviation = np.std(figure4_and_figure5_episodes, axis = 0)
    mean_plus_standard_deviation = mean + standard_deviation
    mean_minus_standard_deviation = mean - standard_deviation
    # Figure 4 Plotting
    plt.axis([0, 300, -256, 100])
    plt.xlabel("Round")
    plt.ylabel("Winnings")
    plt.title("Mean of Each Spin with $256 Limited Bets")
    plt.grid(True)
    plt.plot(mean, label = "mean")
    plt.plot(mean_plus_standard_deviation, label = "mean+")
    plt.plot(mean_minus_standard_deviation, label = "mean-")
    plt.legend()
    plt.savefig("fig4.png")
    plt.clf()
    
    #Figure 5 Calculation
    median = np.median(figure4_and_figure5_episodes, axis = 0)
    standard_deviation = np.std(figure4_and_figure5_episodes, axis = 0)
    median_plus_standard_deviation = median + standard_deviation
    median_minus_standard_deviation = median - standard_deviation
    #Figure 5 Plotting
    plt.axis([0, 300, -256, 100])
    plt.xlabel("Round")
    plt.ylabel("Winnings")
    plt.title("Median of Each Spin with $256 Limited Bets")
    plt.grid(True)
    plt.plot(median, label = "median")
    plt.plot(median_plus_standard_deviation, label = "median+")
    plt.plot(median_minus_standard_deviation, label = "median-")
    plt.legend()
    plt.savefig("fig5.png")
    plt.clf()
        
if __name__ == "__main__": 
    test_code()  		  	   		  		 		  		  		    	 		 		   		 		  
