## 1. Dataset Overview 📊

#### How many games are in the dataset, and over what time period?

- **Number of games:** 16,448  
- **Time period covered:** 1980 to 2020 (40 years)

### What is the distribution of genres, platforms, and publishers?

#### Genres distribution  
<img width="556" height="496" alt="b" src="https://github.com/user-attachments/assets/a80593bd-fe8f-45f2-aa64-cf376d75163a" />



#### Top 10 Platforms distribution  
<img width="287" height="482" alt="a" src="https://github.com/user-attachments/assets/12aeac71-8794-4af2-a035-e07d9bc6d409" />


#### Top 10 Publishers by Number of Games

| Publisher                    | Number of Games |
| ----------------------------|---------------- |
| Electronic Arts             | 1,344           |
| Activision                 | 976             |
| Namco Bandai Games         | 935             |
| Ubisoft                    | 930             |
| Konami Digital Entertainment | 825           |
| THQ                        | 712             |
| Nintendo                   | 700             |
| Sony Computer Entertainment | 686            |
| Sega                       | 631             |
| Take-Two Interactive       | 421             |


---

## **2. Sales Trends 📈**

#### How have **global video game sales** evolved over the years?

<img width="915" height="288" alt="f" src="https://github.com/user-attachments/assets/f6f2f582-090b-4b67-9c53-d75b5ddc4222" />

>The late 1990s and early 2000s mark a major expansion period for the industry, likely driven by new console launches and broader market adoption. After peaking around 2008, sales exhibit a gradual decline through the 2010s, dropping sharply after 2015. This decline in physical global sales from 2010 onwards reflects a broader industry transformation: a shift from physical to digital markets, the rise of mobile gaming, and evolving consumer behavior.

#### How has the number of game releases per year changed over time?
<img width="456" height="352" alt="d" src="https://github.com/user-attachments/assets/62f6a22b-b8cc-4e1d-ab64-9fd362ee7c9d" />

> Video game releases grew steadily from the 1980s, with a sharp rise in the mid-1990s. The peak occurred around 2008–2009, with over 1,400 releases annually. After 2010, the number of releases declined, falling to about 500 by 2016. This drop likely reflects market changes such as digital distribution, mobile gaming growth, and a focus on fewer, higher-quality titles.

#### Are there specific **eras** dominated by certain platforms or genres?

>The data shows distinct shifts in video game genre popularity over three decades:
>1980s: The market was dominated by Platform games (122 sales), followed by Puzzle (63) and Action (51). Many modern genres were just emerging, with very low sales in Simulation and Strategy.
>1990s: There’s a notable rise in Role-Playing (185), Fighting (124), and Sports (146) genres, reflecting growing player interest in immersive and competitive games. Platform games remain strong (209), but Puzzle and Racing games hold smaller shares.
>2000s: Action games explode in popularity with 853 sales, becoming the clear dominant genre. Sports (803) and Shooter (433) genres also see massive growth, indicating a shift toward fast-paced, competitive experiences. Role-Playing and Simulation genres continue to grow steadily.
>Overall, this data illustrates evolving player preferences, from simpler platform and puzzle games in the 80s to a diverse, action and competition-focused market in the 2000s.

#### How do genre preferences differ by **region**?
<img width="572" height="568" alt="g" src="https://github.com/user-attachments/assets/b6b52f76-a2b3-48db-b332-7c836c6aff9e" />

> North America and Europe favor Action, Shooter, and Sports games, while Japan strongly prefers Role-Playing and Fighting genres. Other regions have smaller sales but lean toward Action and Sports. Overall, genre popularity varies distinctly by region.

---

## **3. Review Scores & Sales ⭐**
* Is there a correlation between **Critic Score** and **total sales**?
  > Critic Score & Total Sales (0.20) → Weak positive correlation: higher critic scores tend to be associated with slightly higher sales, but the effect is small.

* Is there a correlation between **User Score** and sales?
  > User Score & Total Sales (0.07) → Almost no correlation: user ratings barely relate to sales.

* Is there a correlation between **User Score** and **Critic Score**?
> Critic Score & User Score (0.50) → Moderate positive correlation: games rated highly by critics often also receive good user ratings, but there are enough disagreements to show divergence.


<img width="447" height="370" alt="i" src="https://github.com/user-attachments/assets/318e8598-5a94-4dad-a6a3-d2d12a86feeb" />



---

## **4. Predictive Insights 🔮**

<img width="712" height="424" alt="j" src="https://github.com/user-attachments/assets/ee53c28b-fa5c-40cf-a3ca-bdeddba13f1f" />

#### Predictive insights: Methodology
To understand what drives a video game’s global sales and make data-driven predictions, we built a Random Forest Regressor model. This choice was deliberate: Random Forests handle both numerical data (like review scores) and categorical data (like genre or platform) with ease, are resilient against overfitting, and—crucially—provide feature importance scores, helping us see which factors truly matter.

The dataset was split into training (80%) and testing (20%) subsets to ensure a fair evaluation of model performance. Numerical features, such as Critic Score and User Score, were used directly, while categorical features, such as Genre or Publisher, were one-hot encoded—transformed into binary variables so the model could process them effectively.

After training the model on the training set, we used it to predict sales in the testing set and evaluated its accuracy using Root Mean Squared Error (RMSE). This end-to-end process not only allowed us to forecast sales but also to pinpoint the features with the greatest predictive power—insights that directly inform strategic recommendations for future game releases.

#### Outcomes


**1. Based on historical data, what factors best predict a game’s global sales?**

* The strongest predictors are **Critic Score** (importance = 0.22) and **Year of Release** (0.18), followed by **User Score** (0.11).
* Certain **publishers** (Nintendo, Take-Two Interactive) and **platform-genre combinations** (Platform, Racing, Shooter, Role-Playing) also play a meaningful role.
* Platform-specific effects (e.g., DS, GB, Wii, PC) add incremental predictive power.


**2. Which platform-genre combination is likely to perform well in future releases?**

* **Nintendo platforms** (Wii, DS, GB) paired with **Platform** and **Role-Playing** genres historically show strong performance.
* **Shooter** and **Racing** genres perform well on high-capability consoles, particularly when supported by major publishers.
* Established genre-platform synergies (e.g., **Platform games on Nintendo consoles**) tend to outperform experimental combinations in sales longevity.



**3. Can review scores be used to forecast commercial success?**

* **Critic Score** has a moderate positive correlation with sales (0.20) and is the single strongest numerical predictor in the model.
* **User Score** correlates weakly (0.07) but still contributes to predictions, especially when combined with critic reviews.
* Exceptions exist:

  * 1,317 high-rated but low-selling games (often niche or poorly marketed).
  * 9 low-rated but high-selling games (franchise-driven or heavily marketed blockbusters).
* Conclusion: Review scores are **helpful but not decisive**; marketing, platform reach, and franchise recognition can override ratings.

--- 

## **5. Business Recommendations 💡**

**If a new game were to be launched in 2026…**

* **Platform & Genre Target**
  Historical sales patterns and feature importance analysis suggest that **Nintendo platforms** (particularly *Switch* successors, given past Wii/DS dominance) combined with **Shooter**, **Role-Playing**, or **Platformer** genres have shown strong performance. While Nintendo-exclusive genres like *Platform* games remain profitable, *Shooter* and *Role-Playing* titles can achieve strong cross-platform appeal.

* **Markets to Prioritize**
  The **North American** and **European** markets account for the majority of global sales, especially for Nintendo and action-oriented titles. Japan remains a significant secondary market, particularly for Role-Playing and Platform games, but should be targeted with localized content and marketing.

* **Minimum Critic Score for Strong Sales**
  Analysis shows a positive but moderate correlation between *Critic Score* and sales (0.20). Titles with **Critic Scores above 80/100** are much more likely to break into the high-sales tier, while those above 85 tend to sustain sales momentum over time. Achieving this level should be a key goal in development and QA phases.

