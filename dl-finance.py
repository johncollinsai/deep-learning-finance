#!/usr/bin/env python
# coding: utf-8

# # Introduction

# ***In this post I discuss some of the papers I have read and found useful when considering deep learning in finance. I discuss academic literature here because a rigorous consideration of deep learning in finance is important, imho. This is my attempt at that and I hope it provides some useful background and context to my subsequent posts.***

# # Deep learning

# Shallow NN-like models with relatively few neuron connections (thus computational stages) have been around for many decades, if not centuries.  Early NN architectures (see for example, McCulloch & Pitts (1943)) did not learn.  Early formulations of unsupervised learning (UL) were published a few years later (Hebb (1949)). The following decades saw simple NNs trained by supervised learning (SL) (see for example, Narendra & Thathatchar (1974), Widrow & Hoff (1962), and Rosenblatt (1958, 1962)) and UL (Willshaw & von der Malsburg (1976), von der Malsburg (1973), Kohonen (1972), and Grossberg (1969)). But it may be argued that NNs were formulated earlier, since early supervised NNs were essentially variants of linear regression methods introduced at the start of the seventeenth century (for example Gauss (1809, 1821), and Legendre (1805)).
# $\\[0.1in]$

# Models with several successive nonlinear layers of neurons were introduced in the 1960's (see for example Ivakhnenko (1968, 1971),  Ivakhnenko, Lapa & McDonough (1967), and Ivakhnenko & Lapa (1965)) and minimization of errors through GD  (Hadamard (1908) in the parameter space of complex, nonlinear, differentiable, multi-stage, NN-related systems were also introduced from this time (for example Director & Rohrer (1969), Bryson & Ho (1969), Amari (1967), Wilkinson (1965), Dreyfus (1962), Bryson & Denham (1961), Pontryagin, Boltyanskii, Gamrelidze & Mishchenko (1961), Bryson (1961), and Kelley (1960)). Efficient GD  methods for SL in discrete, differentiable networks of arbitrary depth called back propagation (BP) were developed in the 1960's and 1970's, and applied to NN's from the early 1980's (see for example LeCun (1988, 1985), Parker (1985), and Werbos (1981)). BP-based training of deep NNs with many layers, however, had been found to be difficult in practice by the late 1980's and it seemed clear that BP by itself suffered quite serious limitations (see Goodfellow, Bengio & Courville (2016) for a review). Networks trained by the group method of data handling (GMDH) Ivakhnenko (1968, 1971),  Ivakhnenko, Lapa & McDonough (1967), and Ivakhnenko & Lapa (1965)) were perhaps the first DL systems of the feed-forward multilayer perceptron type. The units of GMDH NNs had more polynomial activation functions implementing Kolmogorov-Gabor polynomials and were thus more general than other widely used NN activation functions. Given a training set, layers were incrementally grown and trained by regression analysis, then reduced with the help of a separate validation set, using decision regularization to eliminate superfluous units. The numbers of layers and units per layer were learned in problem-dependent modalities. GMDH NNs thus constituted perhaps the first examples of open-ended, hierarchical representation learning with DL (see Schmidhuber (2015) and Russell, Norvig, Canny, Malik, & Edwards (1995) for reviews).
# $\\[0.1in]$

# NNs with many layers had, by the 1990's, become an explicit research subject. Following from the difficulties encountered training deep feed-forward recurrent NNs (RNNs) by BP, Hochreiter (1991) formally identified a major reason: typical deep NNs suffer from so-called vanishing (or exploding) gradients. Hochreiter (1991) showed that with standard activation functions, cumulative back-propagated error signals either shrink rapidly, or grow out of bounds. In fact they decay exponentially with the number of layers, or they explode. This phenomenon was also described as the long time lag problem (see for example Bengio, Simard & Frasconi (1994)). Much subsequent research, particularly in the 1990's and 2000's, was motivated by this insight (see for example Pascanu, Mikolov & Bengio (2013), Hochreiter, Bengio, Paolo & Schmidhuber (2001), Hochreiter & Schmidhuber (1997)).
# $\\[0.1in]$

# DL became practically feasible to some extent through the help of UL. Schmidhumber (2013, 1992) showed that a working 'very deep learner' could perform credit assignment across hundreds of nonlinear operators or neural layers, by using unsupervised pre-training for a hierarchy of RNNs. Schmidhuber showed that the RNN stack may be considered as essentially a deep generative model of the data. Adding another RNN to the stack improved a bound on the data's description length, equivalent to the negative logarithm of its probability (this followed Huffman (1952), and Shannon (1948)), for as long as there is remaining local learnable predictability in the data representation on the corresponding level of the hierarchy. The system was shown to be able to learn many previously unlearnable DL tasks. Stacks of RNNs were used in later work on SL with considerable success, leading not least to the seminal supervised long short-term memory (LSTM) RNN (Perez-Ortiz, Gers, Eck, & Schmidhuber (2003), and Gers, Schmidhuber & Cummins (2000), and Hochreiter & Schmidhuber (1997)). 
# $\\[0.1in]$

# Whilst learning networks with numerous non-linear layers can therefore be seen to date back at least to the 1960's, and explicit DL research results have been published since at least the early 1990's, the expression 'deep learning' only emerged in the mid-2000's, when unsupervised pre-training of deep FNNs helped to accelerate subsequent SL through BP (for example, Hinton, Osindero & Teh (2006), and Hinton & Salakhutdinov (2006)). The 1990's and 2000's also saw many improvements of purely supervised DL, so that many contemporaneous practical applications by researchers and practitioners alike continued to focus upon SL. Several methods, however, used additional UL to facilitate SL. These included the use of recursive auto-associative memory (RAAM) as unsupervised pre-processors to facilitate deep credit assignment for reinforcement learning (RL) (Sutton & Barto (2018) provide a detailed review of RL). Deep NNs became progressively more relevant for RL, where there is no supervising teacher. Schmidhuber (2015) argued that it is beneficial to consider SL and UL together for both scholarly and practical purposes because often gradient-based methods, such as BP, were used to optimize the objective functions of both UL and SL, so that the boundaries between SL and UL may be blurred in many respects. This may be particularly so in the case of time series forecasting.
# $\\[0.1in]$

# A NN's topology may change over time (see for example Goodfellow, Bengio, & Courville (2016) and Schmidhuber (2015)). But at any given moment, it may be described as a finite subset of units (also, nodes or neurons) $N = \{u_1, u_2, ..., \}$ and a finite set $H \subseteq N \times N$ of directed edges (or connections) between nodes. The first (i.e. input) layer is the set of input units, a subset of $N$. In FNNs, the $k$-th layer $\left( k > 1 \right)$ is the set of all nodes $u \in N$ such that there is an edge path of length $k - 1$ (but no longer path) between some input unit and $u$. There may be shortcut connections between distant layers. The NNs behavior (or program) is determined by a set of real-valued, possibly modifiable, parameters (or weights) $w_i \left( i = 1, 2, ..., n \right)$. A single finite episode of information processing and activation spreading, initially without learning through weight changes, is called an epoch. During an epoch, there is a partially causal sequence $x_t \left( t = 1, 2, ..., T \right)$ of real-valued events. Each $x_t$ is either an input set by the environment, or the activation of a unit that may directly depend on other $x_k \left( k < t \right)$ through a current NN topology-dependent set ${in}_t$ of indices $k$ representing incoming causal connections or links. Let the function $v$ encode topology information and map such event index pairs $\left( k, t \right)$ to weight indices. For example, in the non-input case I may have $x_t = f_t \left( \mathrm{net}_t \right)$ with real-valued $\mathrm{net}_t = \sum_{k \in {in}_t} x_k w_{v \left(k, t \right)}$ (additive case) or $\mathrm{net}_t = \prod_{k \in {in}_t} x_k w_{v \left(k, t \right)}$ (multiplicative case), where $f_t$ is a typically nonlinear real-valued activation function (for example, $\mathrm{tanh}$). In this set up, many of the $x_t$ may refer to different, time-varying activations of the same unit (see for example Williams (1989)). During an epoch, the same weight may get reused repeatedly in topology-dependent ways. Schmidhuber (2015) describes this as 'weight sharing across space and/or time'. 
# $\\[0.1in]$

# In SL, certain NN output events $x_t$ may be associated with teacher-given, real-valued labels or targets $d_t$, yielding errors $e_t$, so that $e_t = \frac {1} {2} {\left( x_t - d_t \right)}^2$. A typical goal of supervised NN training is to find weights that yield epochs with small total error, $E$, being the sum of $e_t$. The goal is that the NN will generalize well in later epochs, leading to progressively smaller errors on previously unseen sequences of input events. Many alternative error functions for SL and UL are possible (see for example Goodfellow, Bengio, & Courville (2016) and Hastie, Tibshirani & Friedman (2009)). 
# $\\[0.1in]$

# Following an epoch of activation of differentiable $f_t$, a single iteration of GD  through BP computes the changes for all $w_t$ in proportion to:

# \begin{align}
#     \frac{\partial E} {\partial w_i} = \sum_t \frac{\partial E} {\partial \mathrm{net}_t} \frac{\partial \mathrm{net}_t} {\partial w_i} \label{3.1} \tag{3.1}
# \end{align}
# $\\[0.1in]$

# I show how equation $\ref{3.1}$ is applied as an algorithm for the additive case below (see Algorithm 1, Back-propagation), noting that weight $w_i$ is associated with a real-valued variable $\Delta_i$, initialized by $0$. Algorithm 1 is the central learning algorithm for most FNNs and RNNs, including those used in the empirical study of this paper; section 5 'Models' expands considerably upon this.
# $\\[0.1in]$

# *Algorithm 1. Back-propagation: One iteration of BP for RNNs*
# $\\[0.1in]$

# For $t = T, ..., 1$ do  

# $\; \; \; \;$ to compute $\frac{\partial E} {\partial \mathrm{net}_t}$, initialize real-valued error signal variable $\delta_t$ by 0,

# $\; \; \; \;$ if $x_t$ is an input event then continue with next iteration,

# $\; \; \; \;$ if there is an error $e_t$ then $\delta_t := x_t - d_t$,

# $\; \; \; \;$ add to $\delta_t$ the value $\sum_{k \in \mathrm{out}_t} w_{v \left(t, k \right)} \delta_k$,

# $\; \; \; \;$ multiply $\delta_t$ by $f^\prime_t \left( \mathrm{net}_t \right)$,

# $\; \; \; \;$ for all $k \in \mathrm{in}_t$ add to $\Delta_{w_{v \left( k, t \right)}}$ the value $x_k \delta_t$

# End for.

# Change each $w_i$ in proportion to $\Delta_i$ and a small real-valued learning rate.
# $\\[0.1in]$

# In the 2010s NNs were increasingly applied in domains with complex multi-variate correlation structures and nonlinear dynamics. More complex non-linear time series forecasting models such as deep autoregressive (Flunkert, Salinas, & Gasthaus (2017)), predictive state representation (Downey, Hefny, & Gordon (2017)), and the deep state space model (Rangapuram, Seeger, Gasthaus, Stella, Wang, & Januschowski (2018)) were introduced. These models generally used NNs that contain only the most recent state. Higher-order NNs simulate a deterministic finite state machine and may be considered a multiplicative structure of inputs and the most recent hidden state (see for example Giles, Sun, Chen, Lee, & Chen (1989)). Tensor NNs have allowed different hidden-to-hidden weight matrices for every input dimension (see for example Sutskever, Martens, & Hinton (2011)). Higher-order NNs have concatenated a sequence of past hidden states, although the underlying state interactions were linear (see Soltani & Jiang (2016)).  Hierarchical NNs (see Zheng, Yue & Lucey (2016)) have been used to model sequential data at multiple temporal resolutions and earlier work has recently been generalized to capture higher-order interactions using a hidden-to-hidden tensor (see Yu, Zheng, Anandkumar & Yue (2019)).
# $\\[0.1in]$

# DL may employ first-order hidden-state models to approximate the dynamics. In such a setup, a NN with a single cell recursively computes a hidden state $h_{t-1}$ and generates an output $y_t$ from the hidden state $h_t$. This may be expressed thus:

# \begin{align}
#     h_t = f \left(x_t, h_{t-1} ; \theta_f \right), \; \; \; y_t = g \left( h_t ; \theta_g \right) \label{3.2} \tag{3.2}
# \end{align}
# $\\[0.1in]$

# where $f$ is now a state transition function, $g$ is an output function and $\{ \theta_f , \theta_g \}$ are corresponding model parameters. A common parametrization scheme for equation $\ref{3.2}$ applies a nonlinear activation function such as sigmoid $\sigma$ to a linear map of $x_t$ and $h_{t-1}$ as:

# \begin{align}
#     h_t = \sigma \left( W^{hx} x_t + W^{hh} h_{t-1} + b^h \right), \; \; \; x_{t+1} = W^{xh} h_t + b^x \label{3.3} \tag{3.3}
# \end{align}
# $\\[0.1in]$

# where $W^{hx}$, $W^{xh}$, and $W^{hh}$ are transition weight matrices and $b^h$ and $b^x$ are biases.
# $\\[0.1in]$

# Although NNs can approximate any function in theory, the hidden state $h_t$ only depends on the previous state $h_{t-1}$ and the input $x_t$. The above model does not explicitly capture higher-order dynamics and only implicitly encodes long-term dependencies between all historical states $h_0, h_1, ..., h_t$. This limits the representation power of NNs, especially for forecasting in environments with nonlinear dynamics. Hence, instead of using a wide RNN with many hidden units, some researchers (for example Yu, Zheng, Anandkumar & Yue (2019)) have exploited the recurrent cell to design higher-order tensor RNNs that can approximate complex non-linear governing equations.
# $\\[0.1in]$

# Real-world sequences may have long range dependencies that cannot be captured by Markov models, but NNs lack the interpretability that state space models enjoy. Thus, enhancing state space models with NNs is both natural and has quite a rich history. Traditional approaches can be traced back to nonlinear extensions of linear dynamical systems, such as extended or unscented Kalman filters (for example see Julier & Uhlmann, 1997), where both state transition and emission are generalized to nonlinear functions. The idea of parameterization using NNs is at least as early as Ghahramani & Roweis (1999), and is more extensively used in the last decade (for example Karl, Soelch, Bayer & van der Smagt (2017), Krishnan, Shalit & Sontag (2017), Johnson, Duvenaud, Wiltschko, Datta & Adams (2016), Krishnan, Shalit & Sontag (2015), Archer, Park, Buesing, Cunningham & Paninski (2015), Kingma & Welling, 2014 and Rezende, Mohamed & Wierstra (2014)). Enriching the output distribution of NNs with multinomial output or mixture density networks dates from Bishop (1994).  In the last decade more flexible distributions have been used, including restricted Boltzmann machines (RBM) (see Boulanger-Lewandowski, Bengio & Vincent (2012)), along with variational auto-encoders (VAE) (see for example Gregor, Danihelka, Graves, Rezende & Wierstra (2015) and Chung, Kastner, Dinh, Goel, Courville & Bengio (2015)). 
# Also in the last decade stochasticity has been applied to NNs. Bayer & Osendorfer (2014) and Pachitariu & Sahani (2012) incorporated independent latent variables at each time step and NNs have been attached to both latent states and observations (see for example Fraccaro, Sønderby, Paquet & Winther (2016)).
# $\\[0.1in]$

# Though it is probably not their primary application, a broad and growing literature outside of finance has applied LSTM to time series forecasting. Gers, Schraudolph & Schmidhuber (2002) used LSTMs with peephole connections to learn temporal distances. Malhotra, Vig, Shroff & Agarwal (2015) used stacked LSTM networks to detect anomalies in time series. Guo, Xu, Yao, Chen, Aberer & Funaya (2016) proposed an adaptive gradient learning method for RNNs that enabled robust forecasts for time series with outliers and change points. Hsu (2017) incorporated autoencoder into LSTM to improve its forecasting performance. Cinar, Mirisaee, Goswami, Gaussier, Ait-Bachir & Strijov (2017) proposed an extended attention mechanism to capture periods and model missing values in time series. Bandara, K., Bergmeir, C. & Smyl, S. (2017) used LSTMs on groups of similar time series identified by clustering techniques. Laptev, Yosinski, Li & Smyl (2017) applied RNNs to special event forecasting and found that NNs might be a better choice than classical time series methods when the number, the length and the correlation of the time series are high. Che, Purushotham, Cho Sontag & Liu (2018) introduced a GRU-based model with a decay mechanism to capture informative missingness in multivariate time series.
# $\\[0.1in]$

# # Deep learning in finance

# Deep NNs have been used to forecast stock prices since at least the 1980s (see for example White (1988), Kamijo & Tanigawa (1990), and Khan (2011)). More recently, research has shown that NNs are capable of identifying (non-linear) structures in a broader range of financial time series data (see for example Dixon, Klabjan & Bang (2015), Moritz & Zimmermann (2014), Sermpinis, Theoflatos, Karathanasopoulos, Georgopoulos & Dunis (2013), Takeuchi & Lee (2013), Huck (2009, 2010) and At-salakis & Valavanis (2009)).
# $\\[0.1in]$

# Research focused specifically upon volatility forecasting by deep learners started somewhat later, in the 1990's. Early volatility studies used NNs to forecast implied volatilities after training on past volatilities and other options market factors (see for example Roh (2007), Malliaris & Salchenberger (1996) and Donaldson & Kamstra (1996a, 1996b)). This early literature generally compared NNs to GARCH (see for example Maciel, Gomide & Ballini (2016) and Hajizadeh, Seifi, Fazel Zarandi & Turksen (2012)). The usefulness of a semi-nonparametric neural network-GARCH model to capture nonlinear relationships was demonstrated (see Donaldson & Kamstra (1997); it is noteworthy that benchmark NNs were shown to provide superior performance in this research). Shortly after, Hu & Tsoukalas (1999) combined forecasts from four conditional volatility models within a NN architecture and showed that NNs forecast accurately targeted variables during crisis periods. NNs were trained on the squared innovations deriving from a GARCH model (see Arneric, Poklepovic & Aljinovic (2014)), a setup subsequently extended by training a NN heterogeneous autoregression (HAR) with exogenous variables, to yield superior implied volatility forecasts (see Fernandes, Medeiros & Scharth (2014)).
# $\\[0.1in]$

# Since approximately 2017 research that applies deep learning in traditional finance settings has gained considerable traction, creating a much broader, if nascent, literature for financial times series forecasting with deep NNs. The seminal supervised LSTM RNN (Perez-Ortiz, Gers, Eck, & Schmidhuber (2003), and Gers, Schmidhuber & Cummins (2000), and Hochreiter & Schmidhuber (1997)) has formed the basis for much of this work. I now summarize this recent literature and in order to do so, purely for convenience, group it according to the type of data studied. 
# $\\[0.1in]$

# Firstly I summarize the recent research that forecast stock returns. Fischer & Krauss (2017) deployed LSTM networks to predict out-of-sample directional movements on the S&P 500 and showed LSTM networks outperformed memory free classification methods, specifically a random forest and a logistic regression classifier. Ahmed, Smola, Wang, Xing, Zaheer & Zheng (2018) introduced a State Space LSTM (SSL) by generalizing the Latent-LSTM of Zaheer, Ahmed & Smola (2017). The main intuition of this work, motivated by state space models, was to learn dynamics in the state space, rather than in the sample space as per the LSTM RNN. The SSL was shown to be notably superior and more stable than Latent LSTM. Namin & Namin (2018) compared the performance of LSTM to ARIMA to forecast stock and index return time series with monthly stock and index data.  This research showed superior performance from LSTM, with average reduction in error rates obtained from LSTM of between 84-87 percent compared to ARIMA.
# $\\[0.1in]$

# Secondly, I summarize recent literature that forecast volatility with NNs.  Again, the LSTM RNN was the basis for much of this work. Xiong, Nichols & Shen (2016) used LSTM to forecast the volatility of equities data, incorporating data for 25 Google domestic trends as estimators. Working with daily OHLC equities data, this research showed that LSTM provided better predictions over a range of observation windows compared to linear ridge regression and autoregressive GARCH. Bucci (2019) compared the predictive performance of LSTM to to an autoregressive fractionally integrated moving average with the same set of explanatory variables (ARFIMAX) and without determinants (ARFIMA). Benchmarks further included a logistic smooth transition autoregressive model (LSTAR), also entailing exogenous variables (LSTARX), where the number of lags was set relying on the Akaike and the Bayesian Information criteria. This research used RV based on monthly S&P returns data, with volatility predictors assembled from a broad set of macroeconomic and financial variables. LSTM out-of-sample outperformed all the traditional econometric methods and out-of-sample comparisons showed that LSTM provided significant benefit in predicting relations that were expected to be nonlinear, such as between realized volatility and its determinants. Nguyen, Tran, Gunawan & Kohn (2019) introduced the LSTM-SV model, which used LSTM to model the long-term memory and non-linear auto-dependence in volatility dynamics that is not picked up by the classic SV model (Taylor (1982). This led to a prior distribution for the volatility process that was much more flexible than the AR(1) prior used by Taylor. LSTM-SV retained Taylor’s measurement equation and the linear part of the AR(1) process. The non-linear and long-memory parts were captured by the LSTM structure. Working with weekly stock return and daily exchange rate return time series, this research showed that the LSTM-SV model efficiently captured non-linear and long memory effects in stock and exchange rate returns and provided better out-of-sample forecasts than the standard SV model and a non-linearity N-SV model (Yu, Yang & Zhang (2006)). Petnehazi & Gall (2019) used LSTM to compare the forecasting performance of different volatility estimators based upon Daily OHLC data for equities and found only small differences in the predictive performance of close–to–close; Garman–Klass (1980), Parkinson (1980), Rogers–Satchell (1991), and Yang–Zhang (2000) volatility estimators using LSTM and daily OHLC data for equities.
# $\\[0.1in]$

# Thirdly, I summarize recent literature in which NNs are trained on inflation data.  Almosova & Andresen (2019) researched average forecasting performance using inflation data and compared LSTM to an Auto-Regressive model, Random Walk model, Seasonal Auto-Regressive model, Markov-Switching model (MS-AR), and a NN. This research showed that LSTM outperformed all other forecasting techniques, especially at longer horizons, with the RMSFE being approximately one third to one halve of the errors for the classical models. This research also showed that the LSTM has a high degree of sensitivity to hyperparameters, a topic I return to in some detail in section 6.3 'Hyperparameter tuning'. Verstyuk (2019) performed a comparative analysis of LSTM and Vector Auto-Regressions (VARs) in an application to US data on GDP growth, inflation, commodity prices, Fed Funds rate and bank reserves. Verstyuk showed that LSTM dominates VAR in forecasting out-of-sample.  This research also showed that LSTM performed better in interpretability by means of impulse response functions: for example, a shock to the Fed Funds rate variable generated system dynamics that were more plausible according to conventional economic theory.
# $\\[0.1in]$

# Fourthly, I summarize recent literature in which high frequency data was used to forecast financial time series, stocks and volatilities, with deep NNs. Liu, Pantelous & Mettenheim (2018) proposed a hybrid HAR-RV-J-RNN model to forecast the realized volatility  of high frequency data with jumps. HF index data, sparsely sampled at 5-minutes, was used to compute RV based on a 20 year history and compared to the Heterogeneous AutoRegressive model of Realized Volatility with Jumps (HAR-RV-J) (Andersen, Bollerslev & Diebold, 2007) and a RNN. Liu, Pantelous & Mettenheim showed that all three models produced forecasts of similar quality. However, they also showed that the hybrid HAR-RV-J-RNN model and the RNN model were able to achieve the results with a shorter input time frame. Borovkova & Tsiamas (2019) proposed an ensemble of LSTM for intraday stock price direction predictions, using a large variety of technical analysis indicators as network inputs. This research used stacked LSTM NNs with layer normalization training on HF equities data (22 US large cap stocks), sampled at 5-minute intervals and observed over 1 year, to yield approximately 19,000 observations per stock.  This research built the LSTM ensemble with weighting of individual models proportionate to their recent performance, which allowed the authors to deal with potential non-stationarities in an innovative way. The predictions from each model were evaluated by the area under the curve (AUC) score of the receiver operating characteristic (see ROC; Kent, 1989).  With this set up, the proposed model was found to perform better than benchmark models, LASSO and ridge logistic classifiers, and equally weighted ensembles. Kim & Kim (2019) proposed a feature fusion long short-term memory convolutional neural network (LSTM-CNN), which combined features learned from different representations of the same data, namely prices time series and chart images of the same data. This research worked with HF equity ETF data sampled at 1-minute intervals to yield approximately 97,000 observations. Single models for CNN and LSTM respectively trained on the data showed that LSTM-CNN outperformed single LSTM and CNN models in stock price prediction.  A candlestick chart provided the best stock chart image for forecasting stock prices. This research showed that prediction error was efficiently reduced by using a combination of temporal and image features from the same data, rather than using these features separately.
# $\\[0.1in]$

# Finally, Gu, Kelly & Xiu (2020) conducted the first large-scale empirical analysis of the predictive accuracy of machine learning methods in measuring risk premia of the aggregate market and individual stocks using boosted trees, random forests, and NNs. This research investigated nearly 30,000 individual stocks over 60 years and used a predictor set comprised of 94 characteristics for each stock, interactions of each characteristic with eight aggregate time series variables, and 74 industry sector dummy variables, totaling more than 900 baseline signals. Gu, Kelly & Xiu showed that trees and NNs unambiguously improved return prediction with monthly stock-level $R^2$'s between 0.33% and 0.40%. These authors also showed that a portfolio strategy that timed the S&P 500 with neural network forecasts enjoyed an annualized out-of-sample Sharpe ratio of 0.77, versus the 0.51 Sharpe ratio of a buy-and-hold investor. A value-weighted long-short decile spread strategy that took positions based on stock level NN forecasts earned an annualized out-of-sample Sharpe ratio of 1.35, more than double the performance of leading regression-based strategies from the literature.
# $\\[0.1in]$

# # Conclusion

# ***In this post I have described some of the papers I have read and found useful when considering deep learning in finance. I have covered academic literature because a rigorous consideration of deep learning in finance is important, imho. This was my attempt at that and I hope it provides some useful background and context to my subsequent posts.***

# # References

# Abadi, M., Agarwal, A., Barham, P., Brevdo, E., Chen, Z., Citro, C., Corrado, G. S., Davis, A., Dean, J., Devin, M., Ghemawat, S., Goodfellow, I., Harp, A., Irving, G., Isard, M., Jia, Y., Jozefowicz, R., Kaiser, L., Kudlur, M., Levenberg, J., Mane, D., Monga, R., Moore, S., Murray, D., Olah, C., Schuster, M., Shlens, J., Steiner, B., Sutskever, I., Talwar, K., Tucker, P., Vanhoucke, V., Vasudevan, V., Viegas, F., Vinyals, O., Warden, P., Wattenberg, M., Wicke, M., Yu, Y. & Zheng, X. (2015). TensorFlow: Large-scale machine learning on heterogeneous systems. http://tensorflow.org/
# $\\[0.05in]$

# Ahmed, A., Smola, A., Wang, Y., Xing, E.P., Zaheer, M. & Zheng, X. (2018). State space LSTM models with particle MCMC inference. arXiv:1711.11179v1.
# $\\[0.05in]$

# Almosova, A. & Andresen, N. (2019). Nonlinear inflation forecasting with recurrent neural networks. Working Paper.
# $\\[0.05in]$

# Amari, S. (1967). A theory of adaptive pattern classifiers. IEEE Trans. EC, 16, 3 299–307.
# $\\[0.05in]$

# Andersen, T.G., Bollerslev, T. & Diebold, F.X. (2007). Roughing it up: Including jump components in the measurement, modelling, and forecasting of return volatility. Review of Economics and Statistics, 2007, 89(4), 701-720.
# $\\[0.05in]$

# Andersen, T.G., Bollerslev, T., Diebold, F.X. & Ebens, H. (2001). The distribution of realized stock return volatility. Journal of Financial Economics 61, 43–76.
# $\\[0.05in]$

# Archer, E., Park, I.M., Buesing, L., Cunningham, J. & Paninski, L. (2015). Black box variational inference for state space models. arXiv:1511.07367.
# $\\[0.05in]$

# Arneric, J., Poklepovic, T. & Aljinovic, Z. (2014). GARCH based artificial neural networks in forecasting conditional variance of stock returns. Croatian Operational Research Review, 5, 329–343.
# $\\[0.05in]$

# Bandara, K., Bergmeir, C. & Smyl, S. (2017). Forecasting across time series databases using recurrent neural networks on groups of similar series:
# A clustering approach. arXiv:1710.03222.
# $\\[0.05in]$

# Bang-Jensen, J. (2008). Digraphs: Theory, Algorithms and Applications, Springer Monographs. In Mathematics (2nd ed.), Springer-Verlag, 32–34.
# $\\[0.05in]$

# Barndorff-Nielsen, O.E., Shephard, N., 2002. Econometric analysis of realised volatility and its use in estimating stochastic volatility models. Journal of Royal Statistical Society, 64, 253–280.
# $\\[0.05in]$

# Bayer, J. & Osendorfer, C. (2014). Learning stochastic recurrent networks. arXiv:1411.7610.
# $\\[0.05in]$

# Bengio, Y., Lamblin, P., Popovici, D. & Larochelle, H. (2007). Greedy layer-wise training of deep networks. Advances in Neural Information Processing Systems (NIPS’06), 153-160.
# $\\[0.05in]$

# Bengio, Y., Simard, P., & Frasconi, P. (1994). Learning long-term dependencies with gradient descent is difficult. IEEE Transactions on Neural Networks, 5(2), 157–166.
# $\\[0.05in]$

# Bishop, C.M. (1994). Mixture density networks. Technical report, 1994.
# $\\[0.05in]$

# Borovkova, S. & Tsiamas, I. (2018). An ensemble of LSTM neural networks for high frequency stock market classification. Journal of Forecasting, 38, 600-619.
# $\\[0.05in]$

# Boulanger-Lewandowski, N., Bengio, Y. & Vincent, P. (2012). Modeling temporal dependencies in high-dimensional sequences: Application to polyphonic music generation and transcription. In ICML, 2012.
# $\\[0.05in]$

# Bryson, A. E. (1961). A gradient method for optimizing multi-stage allocation processes. In Proc. Harvard Univ. Symposium on digital computers and their applications.
# $\\[0.05in]$

# Bryson, Jr., A. E. & Denham, W. F. (1961). A steepest-ascent method for solving optimum programming problems. Technical Report BR-1303, Raytheon Company, Missle and Space Division.
# $\\[0.05in]$

# Bryson, A. & Ho, Y. (1969). Applied optimal control: optimization, estimation, and control. Blaisdell Pub. Co.
# $\\[0.05in]$

# Bucci, A. (2019). Realized volatility forecasting with neural networks. MPRA Paper No. 95443. Online at https://mpra.ub.uni-muenchen.de/95443/.
# $\\[0.05in]$

# Che, Z.P., Purushotham, S., Cho, K.Y., Sontag, D., & Liu, Y. (2018). Recurrent neural networks for multivariate time series. Scientific reports, 8(1), 6085.
# $\\[0.05in]$

# Cho, K.H., Chung, J.Y., Gulcehre, C. & Bengio, Y. (2014). Empirical evaluation of gated recurrent neural networks on sequence modeling. arXiv preprint arXiv:1412.3555, 2014.
# $\\[0.05in]$

# Chollet, F. (2015). Keras. https://keras.io.
# $\\[0.05in]$

# Chollet, F. (2018). Deep learning with Python. Manning, Shelter Island.
# $\\[0.05in]$

# Chung, J.Y., Kastner, K., Dinh, L., Goel, K., Courville, A. & Bengio, Y. (2015). A recurrent latent variable model for sequential data. In NIPS, 2015.
# $\\[0.05in]$

# Cinar, Y.G., Mirisaee, H., Goswami, P., Gaussier, E, Ait-Bachir, A. & Strijov, F.V. (2017). Time series forecasting using RNNs: an extended attention mechanism to model periods and handle missing values. CoRR, abs/1703.10089.
# $\\[0.05in]$

# Collins, J.L. (2020). Multifractal volatility predictions with a high-dimensional state space using high frequency data with suppressed microstructure noise. Unpublished paper.
# $\\[0.05in]$

# Connor, J.T., Douglas Martin, R. & Atlas, L.E. (1994). Recurrent neural networks and robust time series prediction. IEEE transactions on neural networks, Vol. 5, No. 2, 240-254.
# $\\[0.05in]$

# de Vries, B. & Principe, J.C. (1991). A theory for neural networks with time delays. In Lippmann, R.P., Moody, J.E. & Touretzky, D.S. (Eds), Advances in Neural Information Processing Systems 3, Morgan Kaufmann. 162–168.
# $\\[0.05in]$

# Director, S. W. & Rohrer, R. A. (1969). Automated network design - the frequency-domain case. IEEE Trans. Circuit Theory, CT, 16, 330–337.
# $\\[0.05in]$

# Dixon, M., Klabjan, D. & Bang, J.H. (2015). Implementing deep neural networks for fnancial market prediction on the Intel Xeon Phi. In: roceedings of the 8th Workshop on High Performance Computational Finance. 1-6.
# $\\[0.05in]$

# Dixon, M., Klabjan, D. & Bang, J.H. (2017). Classification-based financial markets prediction using deep neural networks. Algorithmic Finance, 6, 67–77
# $\\[0.05in]$

# Donaldson, G.R. & Kamstra, M. (1996a). A new dividend forecasting procedure that rejects bubbles in asset prices. Review of Financial Studies, 8, 333–383.
# $\\[0.05in]$

# Donaldson, G.R. & Kamstra, M. (1996b). Forecast Combining with Neural Networks. Journal of Forecasting, 15, 49–61.
# $\\[0.05in]$

# Donaldson, G.R. & Kamstra, M. (1997). An artificial neural network-GARCH model for international stock return volatility. Journal of Empirical Finance 4, 17–46.
# $\\[0.05in]$

# Downey, C., Hefny, A. & Gordon, G. (2017). Practical learning of predictive state representations. arXiv preprint arXiv:1702.04121.
# $\\[0.05in]$

# Dreyfus, S. E. (1962). The numerical solution of variational problems. Journal of Mathematical Analysis and Applications, 5, 30–45.
# $\\[0.05in]$

# Faraway, J. & Chatfield, C. (1998). Time series forecasting with neural networks: a comparative study using the air line data. Journal of the Royal Statistical Society: Series C (Applied Statistics), 47(2), 231-250.
# $\\[0.05in]$

# Fernandes, M., Medeiros, M.C., Scharth, M., 2014. Modeling and predicting the CBOE market volatility index. Journal of Banking & Finance, 40, 1–10.
# $\\[0.05in]$

# Fischer, T. & Krauss, C. (2017). Deep learning with long short term memory networks for financial market predictions. FAU Discussion Papers in Economics, No. 11/2017, Friedrich-Alexander-Universität Erlangen-Nürnberg, Institute for Economics, Erlangen.
# $\\[0.05in]$

# Flunkert, V., Salinas, D. & Gasthaus, J. (2017). Deepar: Probabilistic forecasting with autoregressive recurrent networks. arXiv preprint arXiv:1704.04110, 2017.
# $\\[0.05in]$

# Fraccaro, M., Sønderby, S.K., Paquet, U. & Winther, O. (2016). Sequential neural models with stochastic layers. In NIPS, 2016.
# $\\[0.05in]$

# Garman, M. B. & Klass, M. J. (1980). On the estimation of security price volatilities from historical data. Journal of Business, 53(1), 67–78.
# $\\[0.05in]$

# Graves, A., Liwicki, M., Fernandez, S., Bertolami, R., Bunke, H. & Schmidhuber, J. (2009). A Novel connectionist system for improved unconstrained handwriting recognition. IEEE Transactions on Pattern Analysis and Machine Intelligence, 31, 5.
# $\\[0.05in]$

# Gauss, C. F. (1809). Theoria motus corporum coelestium in sectionibus conicis solem ambientium.
# $\\[0.05in]$

# Gauss, C. F. (1821). Theoria combinationis observationum erroribus minimis obnoxiae (Theory of the combination of observations least subject to error).
# $\\[0.05in]$

# Gers, F. A., Schmidhuber, J., & Cummins, F. (2000). Learning to forget: Continual prediction with LSTM. Neural Computation, 12, 2451–2471.
# $\\[0.05in]$

# Gers, F.A., Schraudolph, N.N. & Schmidhuber, J. (2002). Learning precise timing with LSTM recurrent networks. Journal of machine learning research, 3, 115-143.
# $\\[0.05in]$

# Ghahramani, Z. & Roweis, S.T. (1999). Learning nonlinear dynamical systems using an EM algorithm. In NIPS, 1999.
# $\\[0.05in]$

# Giles, C.L., Lawrence, S. & Tsoi, A.C. (2001). Noisy time series prediction using recurrent neural networks and grammatical inference. Machine learning 44, 1, 161-183.
# $\\[0.05in]$

# Giles, C.L., Sun, G.Z., Chen, H.H., Lee, Y.C. & Chen, D. (1989). Higher order recurrent networks and grammatical inference. NIPS, 380-387.
# $\\[0.05in]$

# Gisslen, L., Luciw, M., Graziano, V. & Schmidhuber, J. (2011). Sequential constant size compressor for reinforcement learning. In Proc. Fourth Conference on Artificial General Intelligence (AGI), Google, Mountain View, CA, 31–40. Springer.
# $\\[0.05in]$

# Gomez, F., Schmidhuber, J. & Miikkulainen, R. (2008). Accelerated neural evolution through cooperatively coevolved synapses. Journal of Machine Learning Research, 9, 937-965.
# $\\[0.05in]$

# Goodfellow, I., Bengio, Y. & Courville, A. (2016). Deep Learning, MIT Press.
# $\\[0.05in]$

# Graves, A. (2014). Generating sequences with recurrent neural networks. arXiv:1308.0850v5.
# $\\[0.05in]$

# Graves, A., Mohamed, A. & Hinton, G. (2013). Speech recognition with deep recurrent neural networks. arXiv:1303.5778.
# $\\[0.05in]$

# Graves, A. & Schmidhuber, J. (2005). Framewise phoneme classification with bidirectional LSTM and other neural network architectures. Neural Networks 18:5-6, 602-610.
# $\\[0.05in]$

# Greff, K., Srivastava, R.K., Koutnik, J., Steunebrink, B.R. & Schmidhuber, J. (2017). LSTM: A search space odyssey. IEEE transactions on neural
# networks and learning systems, 28(10), 2222-2232.
# $\\[0.05in]$

# Gregor, K., Danihelka, I, Graves, A., Rezende, D.J. & Wierstra, D. (2015). DRAW: A recurrent neural network For image generation. In ICML, 2015.
# $\\[0.05in]$

# Grossberg, S. (1969). Some networks that can learn, remember, and reproduce any number of complicated space-time patterns, I. Journal of Mathematics and Mechanics, 19, 53–91.
# $\\[0.05in]$

# Grossberg, S. (1988). onlinear neural networks: Principles, mechanisms, and architectures. Neural Networks, 1, 17–61.
# $\\[0.05in]$

# Grossberg, S. (2013). Recurrent neural networks. Scholarpedia, 8(2):1888.
# $\\[0.05in]$

# Gu, S.H., Kelly, B.T. & Xiu, D.C (2020). Empirical asset pricing via machine learning. The Review of Financial Studies, Volume 33, Issue 5, 2223–2273.
# $\\[0.05in]$

# Gu, S.H., Kelly, B.T. & Xiu, D.C (2019). Autoencoder asset pricing models. Yale ICF Working Paper No. 2019-04; Chicago Booth Research Paper No. 19-24.
# $\\[0.05in]$

# Guo, T., Xu, Z., Yao, X, Chen, H.F., Aberer, K. & Funaya, K. (2016). Robust online time series prediction with recurrent neural networks. In Data
# Science and Advanced Analytics (DSAA), 2016 IEEE International Conference, 816-825. Ieee, 2016.
# $\\[0.05in]$

# Hajizadeh, E., Seifi, A., Fazel Zarandi, M. & Turksen, I. (2012). A hybrid modeling approach for forecasting the volatility of S&P 500 index return. Expert Systems with Applications 39, 431–436.
# $\\[0.05in]$

# Hamid, S.A. & Iqbal, Z. (2004). Using neural networks for forecasting volatility of S&P 500 index futures prices. Journal of Business Research, 57, 1116-1125. 
# $\\[0.05in]$

# Harris, C.R., Millman, K.J., van der Walt, S.J., Gommers, R., Virtanen, P., Cournapeau, D., Wieser, E., Taylor, J., Berg, S., Smith, N.J., Kern, R., Picus, M., Hoyer, S., Brett, M., Haldane, A., Fernandez del Rio, A., Wiebe, M., Sheppard, K., Reddy, T., Weckesser, W. & Oliphant, T.E. (2020). Array programming with NumPy. Nature 585, 357–362.
# $\\[0.05in]$

# Hastie, T., Tibshirani, R. & Friedman, J. (2009). The elements of statistical learning: data mining, inference, and prediction. 2Ed, Springer.
# $\\[0.05in]$

# Heaton, J.B., Polson, N.G. & Witte, J.H. (2016). Deep learning in finance, arXiv:1602.06561.
# $\\[0.05in]$

# Hebb, D. O. (1949). The Organization of Behavior. Wiley, New York.
# $\\[0.05in]$

# Hinton, G.E., Osindero, S. & Teh, Y.W. (2006). A fast learning algorithm for deep belief nets. Neural Computation, 18 (7).
# $\\[0.05in]$

# Hinton, G.E. & Salakhutdinov, R. (2006). Reducing the dimensionality of data with neural networks. Science, 313(5786), 504–507.
# $\\[0.05in]$

# Hinton, G.E., Srivastava, N., Krizhevsky, A., Sutskever, I. & Salakhutdinov, R.R. (2012). Improving neural networks by preventing co-adaptation
# of feature detectors. arXiv:1207.0580.
# $\\[0.05in]$

# Hochreiter, S. (1991). Untersuchungen zu dynamischen neuronalen Netzen. Diploma thesis, Institut fur Informatik, Lehrstuhl Prof. Brauer, Technische Universitat Munchen.
# $\\[0.05in]$

# Hochreiter, S. & Schmidhuber, J. (1997). Long short-term memory. Neuralcomputation, 9(8): 1735-1780.
# $\\[0.05in]$

# Hochreiter, S., Bengio, Y., Paolo, F. & Schmidhuber, J. (2001). Gradient flow in recurrent nets: the difficulty of learning long-term dependencies. In Kremer & Kolen (Eds), A Field Guide to Dynamical Recurrent Neural Networks. IEEE Press.
# $\\[0.05in]$

# Hornik, K., Stinchcombe, M. & White, H. (1989). Multilayer feedforward networks are universal approximators. Neural networks 2, 359-366.
# $\\[0.05in]$

# Hornik, K. (1991). Approximation capabilities of multilayer feedforward networks. Neural Networks, 4(2), 251–257.
# $\\[0.05in]$

# Hsu, D. (2017). Time series forecasting based on augmented long short-term memory. arXiv:1707.00666.
# $\\[0.05in]$

# Hu, Y.M. & Tsoukalas, C. (1999). Combining conditional volatility forecasts using neural networks: an application to the EMS exchange rates. Journal of International Financial Markets, Institutions & Money 9, 407–422.
# $\\[0.05in]$

# Huck, N. (2009). Pairs selection and outranking: An application to the S&P 100 index. European Journal of Operational Research 196, 2, 819-825.
# $\\[0.05in]$

# Huck, N. (2010). Pairs trading and outranking: The multi-step-ahead forecasting case. European Journal of Operational Research 207, 3, 1702-1716.
# $\\[0.05in]$

# Huffman, D. A. (1952). A method for construction of minimum-redundancy codes. Proceedings IRE, 40, 1098–1101.
# $\\[0.05in]$

# Ioffe, S. & Szegedy, C. (2015). Batch normalization: accelerating deep network training by reducing internal covariate shift”. arXiv:1502.03167.
# $\\[0.05in]$

# Ivakhnenko, A. G. (1968). The group method of data handling – a rival of the method of stochastic approximation. Soviet Automatic Control, 13, 3, 43–55.
# $\\[0.05in]$

# Ivakhnenko, A. G. (1971). Polynomial theory of complex systems. IEEE Transactions on Systems, Man and Cybernetics, 4, 364–378.
# $\\[0.05in]$

# Ivakhnenko, A. G. & Lapa, V. G. (1965). Cybernetic Predicting Devices. CCM Information Corporation.
# $\\[0.05in]$

# Ivakhnenko, A. G., Lapa, V. G., & McDonough, R. N. (1967). Cybernetics and forecasting techniques.  American Elsevier, NY.
# $\\[0.05in]$

# Israel, R., Kelly, B.T. & Moskowitz, T. (2020). Can machines "learn" finance? Journal of Investment Management, Volume 18, No. 2.
# $\\[0.05in]$

# Johnson, M.J., Duvenaud, D., Wiltschko, A.B., Datta, S.R. & Adams, R.P. (2016). Composing graphical models with neural networks for structured representations and fast inference. In NIPS, 2016.
# $\\[0.05in]$

# Julier, S.J. & Uhlmann, J.K. (1997). A new extension of the Kalman filter to nonlinear systems. In International symposium on aerospace/defense sensing, simulation and controls 1.
# $\\[0.05in]$

# Kamijo, K. & Tanigawa, T. (1990). Stock price pattern recognition - a recurrent neural network approach. 1990 IJCNN International Joint Conference on Neural Networks.
# $\\[0.05in]$

# Karl, M., Soelch, M., Bayer, J. & van der Smagt, P. (2017). Deep variational Bayes filters: Unsupervised learning of state space models from raw data. In ICLR, 2017.
# $\\[0.05in]$

# Karpathy, A., Johnson, J. & Li, F.F. (2015). Visualizing and understanding recurrent networks. arXiv:1506.02078.
# $\\[0.05in]$

# Khan, A.I. (2011). Financial volatility forecasting by nonlinear support vector machine heterogeneous autoregressive model: Evidence from Nikkei 225 Stock Index. International Journal of Economics and Finance 3, 138–150.
# $\\[0.05in]$

# Kingma, D.P. & Welling, M. (2014). Auto-Encoding Variational Bayes. In ICLR, 2014.
# $\\[0.05in]$

# Kelley, H. J. (1960). Gradient theory of optimal flight paths. ARS Journal, 30, 10, 947–954.
# $\\[0.05in]$

# Kim, T. & Kim, H.Y. (2019). Forecasting stock prices with a feature fusion LSTM-CNN model using different representations of the same data. PLoS ONE 14(2): e0212320.
# $\\[0.05in]$

# Kohonen, T. (1988). Self-Organization and Associative Memory. Springer, second edition.
# $\\[0.05in]$

# kornblith, S., Norouzi, M., Lee, H. & Hinton, G.E. (2019). Similarity of neural network representations revisited. Proceedings of the 36th International Conference on Machine Learning, Long Beach, California.
# $\\[0.05in]$

# Krishnan, R.G., Shalit, U. & Sontag, D. (2015). Deep Kalman Filters. arXiv:1511.05121.
# $\\[0.05in]$

# Krishnan, R.G., Shalit, U. & Sontag, D. (2017). Structured inference networks for nonlinear state space models. In AAAI, 2017.
# $\\[0.05in]$

# Kyrychko, Y. & Hogan, S. (2010). On the use of delay equations in engineering applications. 16, 943–960.
# $\\[0.05in]$

# Laptev, N., Yosinski, J., Li, L.E. & Smyl, S. (2017). Time-series extreme event forecasting with neural networks at Uber. In International
# Conference on Machine Learning, 34, pages 1-5.
# $\\[0.05in]$

# LeCun, Y. (1985). Une proc´edure d’apprentissage pour r´eseau `a seuil asym´etrique. Proceedings of Cognitiva 85, Paris, 599–604.
# $\\[0.05in]$

# LeCun, Y. (1988). A theoretical framework for back-propagation. In Touretzky, D., Hinton, G., & Sejnowski, T., editors, Proceedings of the 1988 Connectionist Models Summer School, 21–28, CMU, Pittsburgh, Pa. Morgan Kaufmann.
# $\\[0.05in]$

# LeCun, Y., Bengio, Y. & Hinton, G. (2015). Deep learning. Nature, 521(7553): 436-444.
# $\\[0.05in]$

# Legendre, A. M. (1805). Nouvelles m´ethodes pour la d´etermination des orbites des cometes. F. Didot.
# $\\[0.05in]$

# Lipton, Z., Berkowitz, J. & Elkan, C. (2015). A critical review of recurrent neural networks for sequence learning. arXiv:1506.00019.
# $\\[0.05in]$

# Liu, F., Pantelous, A.A. & von Mettenheim, H.J. (2018). Forecasting and trading high frequency volatility on large indices. Quantitative Finance, Vol. 18, 5, 737-748
# $\\[0.05in]$

# Luo, R., Zhang, W.N., Xu, X.J. & Wang, J. (2018). A neural stochastic volatility model. The Thirty-Second AAAI Conference on Artificial Intelligence (AAAI-18), 6401-6408.
# $\\[0.05in]$

# Maciel, L., Gomide, F. & Ballini, R. (2016). Evolving Fuzzy-GARCH approach for financial volatility modeling and forecasting. Computational Economics 48, 379–398.
# $\\[0.05in]$

# Malhotra, P., Vig, L, Shroff, G. & Agarwal, P. (2015). Long short term memory networks for anomaly detection in time series. In Proceedings, 89. Presses universitaires de Louvain, 2015.
# $\\[0.05in]$

# Malliaris, M. & Salchenberger, L. (1996). Using neural networks to forecast the S&P 100 implied volatility. Neurocomputing, 10(2), 183–195.
# $\\[0.05in]$

# Mayer, H., Gomez, F., Wierstra, D., Nagy, I., Knoll, A. & Schmidhuber, J. (2008). A system for robotic heart surgery that learns to tie knots using recurrent neural networks. Advanced Robotics, 22/13-14, 1521-1537.
# $\\[0.05in]$

# McCulloch, W. & Pitts, W. (1943). A logical calculus of the ideas immanent in nervous activity. Bulletin of Mathematical Biophysics, 7, 115–133.
# $\\[0.05in]$

# Metropolis, N., Rosenbluth, A., Rosenbluth, M., Teller, A. & Teller, E. (1953). Equation of state calculations by fast computing machines. Journal of Chemical Physics, 21, 1087.
# $\\[0.05in]$

# Metropolis, N., Rosenbluth, A., Rosenbluth, M., Teller, A. & Teller, E. (1953). Equation of state calculations by fast computing machines. Journal of Chemical Physics, 21, 1087.
# $\\[0.05in]$

# Minsky, M.L. & Papert, S.A. (1990). Perceptrons, 2nd Ed. MIT Press, Cambridge MA.
# $\\[0.05in]$

# Moritz, B. & Zimmermann, T. (2014). Deep conditional portfolio sorts: The relation between past and future stock returns. Working paper, LMU Munich and Harvard University.
# $\\[0.05in]$

# Namin, S.S. & Namin, S.N. (2018). Forecasting economic and financial time series: ARIMA vs. LSTM. Working Paper.
# $\\[0.05in]$

# Narendra, K. S. & Thathatchar, M. A. L. (1974). Learning automata – a survey. IEEE Transactions on Systems, Man, and Cybernetics, 4, 323–334.
# $\\[0.05in]$

# Nguyen, N., Tran, M.N., Gunawan, D. & Kohn, R. (2019). A long short-term memory stochastic volatility model. arXiv:1906.02884v2 [
# econ.EM] 30 Sep 2019.
# $\\[0.05in]$

# Parker, D. B. (1985). Learning-logic. Technical Report TR-47, Center for Comp. Research in Economics and Management Sci., MIT.
# $\\[0.05in]$

# Perez-Ortiz, J. A., Gers, F. A., Eck, D., & Schmidhuber, J. (2003). Kalman filters improve LSTM network performance in problems unsolvable by traditional recurrent nets. Neural Networks, 16, 241–250.
# $\\[0.05in]$

# Pachitariu, M. & Sahani, M. (2012). Learning visual motion in recurrent neural networks. In NIPS, 2012.
# $\\[0.05in]$

# Parkinson, M. (1980). The extreme value method for estimating the variance of the rate of return. Journal of Business, 53(1), 61–65.
# $\\[0.05in]$

# Pascanu, R., Mikolov, T. & Bengio, Y. (2013). On the difficulty of training recurrent neural networks. In International Conference on Machine Learning, 1310–1318.
# $\\[0.05in]$

# Paszke, A., Gross, S., Massa, F., Lerer, A., Bradbury, J., Chanan, G., Killeen, T., Lin, Z., Gimelshein, N., Antiga, L., Desmaison, A., Kopf, A., Yang, E., DeVito, Z., Raison, M., Tejani, A., Chilamkurthy, S., Steiner, B., Fang, L., Bai, J. & Chintala, S. (2019). PyTorch: An Imperative Style, High-Performance Deep Learning Library. In Wallach, H., Larochelle, H., Beygelzimer, A., Fox, E. & Garnett, R. (Eds.), Advances in Neural Information Processing Systems 32, Curran Associates, Inc. https://pytorch.org/ 
# $\\[0.05in]$

# Patel, A.B., Nguyen, T. & Baraniuk, R.G. (2015). A probabilistic theory of deep learning. Rice University Electrical and Computer Engineering Dept. Technical Report No 2015-1. arXiv:1504.00641
# $\\[0.05in]$

# Petnehazi, G. & Gall, J. (2019). Exploring the predictability of range‐based volatility estimators using recurrent neural networks. Intell Sys Acc Fin Mgmt. 2019; 1–8.
# $\\[0.05in]$

# Petnehazi, G. (2019). Recurrent neural networks for time series forecasting. arXiv:1901.00069v1 [cs.LG].
# $\\[0.05in]$

# Pontryagin, L. S., Boltyanskii, V. G., Gamrelidze, R. V., & Mishchenko, E. F. (1961). The Mathematical Theory of Optimal Processes.
# $\\[0.05in]$

# Rangapuram, S.S., Seeger, M., Gasthaus, J., Stella, L., Wang, Y.Y. & Januschowski, T. (2018). Deep state space models for time series forecasting. 32nd Conference on Neural Information Processing Systems (NeurIPS 2018).
# $\\[0.05in]$

# Rezende, D.J., Mohamed, S. & Wierstra, D. (2014). Stochastic backpropagation and approximate inference in deep generative models. In ICML, 2014.
# $\\[0.05in]$

# Richard, J.P. (2003). Time delay systems: An overview of some recent advances and open problems. Automatica, 39, 10, 1667–1694.
# $\\[0.05in]$

# Rogers, L. C. G. & Satchell, S. E. (1991). Estimating variance from high, low and closing prices. The Annals of Applied Probability, 1(4), 504–512.
# $\\[0.05in]$

# Roh, T. H. (2007). Forecasting the volatility of stock price index. Expert Systems with Applications, 33(4), 916–922.
# $\\[0.05in]$

# Rosenblatt, F. (1958). The perceptron: a probabilistic model for information storage and organization in the brain. Psychological review, 65(6), 386.
# $\\[0.05in]$

# Rosenblatt, F. (1962). Principles of Neurodynamics. Spartan, New York.
# $\\[0.05in]$

# Russell, S. J., Norvig, P., Canny, J. F., Malik, J. M., & Edwards, D. D. (1995). Artificial Intelligence: a Modern Approach, Vol 2. Englewood Cliffs: Prentice Hall.
# $\\[0.05in]$

# Schmidhuber, J. (1992). Learning complex, extended sequences using the principle of history compression. Neural Computation, 4(2), 234–242.
# $\\[0.05in]$

# Schmidhuber, J., Wierstra, D., Gagliolo, M. & Gomez, F. (2007). Training recurrent networks by Evolino. Neural Computation, 19(3), 757-779.
# $\\[0.05in]$

# Schmidhuber, J. (2013). My first Deep Learning system of 1991 + Deep Learning timeline 1962-2013. Technical Report arXiv:1312.5548v1 [cs.NE], The Swiss AI Lab IDSIA.
# $\\[0.05in]$

# Schmidhuber, J. (2015). Deep learning in neural networks: An overview. Neural networks, 61, 85–117.
# $\\[0.05in]$

# Sermpinis, G., Theoflatos, K., Karathanasopoulos, A., Georgopoulos, E.F. & Dunis, C. (2013). Forecasting foreign exchange rates with adaptive neural networks using radial-basis functions and particle swarm optimization. European Journal of Operational Research 225, 3, 528-540.
# $\\[0.05in]$

# Sezer, O.B., Gudelek, M.U. & Ozbayoglu, A.M. (2019). Financial time series forecasting with deep learning: a systematic literature review 2005-2019. arXiv:1911.13288v1
# $\\[0.05in]$

# Shannon, C. E. (1948). A mathematical theory of communication (parts I and II). Bell System Technical Journal, XXVII, 379–423.
# $\\[0.05in]$

# Sherstinsky, A. & Picard, R.W. (1998). On stability and equilibria of the M-Lattice. IEEE Transactions on Circuits and Systems – I: Fundamental Theory and Applications, 45, 4, 408–415.
# $\\[0.05in]$

# Sherstinsky, A. (2018a). Deriving the Recurrent Neural Network Definition and RNN Unrolling Using Signal Processing. In Critiquing and Correcting Trends in Machine Learning Workshop, NeurIPS 31.
# 2018), Dec 2018.
# $\\[0.05in]$

# Sherstinsky, A. (2018b). Fundamentals of Recurrent Neural Network (RNN) and Long Short-Term Memory (LSTM) Network, arxiv:1808.03314.
# $\\[0.05in]$

# Sherstinsky, A. (2020). Fundamentals of recurrent neural network (RNN) and long short-term memory (LSTM) network. Physica D: Nonlinear Phenomena, Volume 404, March 2020: Special Issue on Machine Learning and Dynamical Systems.
# $\\[0.05in]$

# Siah, K. W. & Myers, P. (2016). Stock market prediction through technical and public sentiment analysis. Available online at http://kienwei.mit.edu/sites/default/files/images/stock-market-prediction.pdf
# $\\[0.05in]$

# Siegelmann, H. T. & Sontag, E. D. (1991). Turing computability with neural nets. Applied Mathematics Letters, 4(6), 77–80.
# $\\[0.05in]$

# Soltani, R. & Jiang, H. (2016). Higher order recurrent neural networks. arXiv:1605.00064.
# $\\[0.05in]$

# Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I. & Salakhutdinov, R. (2014). Dropout: A simple way to prevent neural networks from over-fitting. Journal of Machine Learning Research, 15(1), 1929-1958.
# $\\[0.05in]$

# Sutskever, I., Martens, J. & Hinton, G.E. (2011). Generating text with recurrent neural networks. In Proceedings of the 28th International Conference on Machine Learning (ICML-11), 1017-1024.
# $\\[0.05in]$

# Sutton, R.S. & Barto, A.G. (2018). Reinforcement learning, an introduction. 2nd Ed. The MIT Press, Cambridge, MA.
# $\\[0.05in]$

# Tang, Z.Y., De Almeida, C. & Fishwick, P.A. (1991). Time series forecasting using neural networks vs. box-jenkins methodology. Simulation, 57(5), 303-310, 1991.
# $\\[0.05in]$

# Takeuchi, L. & Lee, Y.Y. (2013). Applying deep learning to enhance momentum trading strategies in stocks. Working paper, Stanford University.
# $\\[0.05in]$

# Verstyuk, S. (2019). Modeling multivariate time series in economics: from auto-regressions to recurrent neural networks. Unpublished paper.
# $\\[0.05in]$

# Van der Westhuizen, J. &  Lasenby, J. (2017). Visualizing LSTM decisions. Stat, 1050:23.
# $\\[0.05in]$

# Von der Malsburg, C. (1973). Self-organization of orientation sensitive cells in the striate cortex. Kybernetik, 14(2), 85–100.
# $\\[0.05in]$

# Vortelinos, D.I., 2017. Forecasting realized volatility: HAR against Principal Components Combining, neural networks and GARCH. Research in International Business and Finance, 39, 824–839.
# $\\[0.05in]$

# Werbos, P.J (1974). Beyond regression: new tools for prediction and analysis in the behavioral sciences. Ph. D. dissertation, Harvard University.
# $\\[0.05in]$

# Werbos, P. J. (1981). Applications of advances in nonlinear sensitivity analysis. In Proceedings of the 10th IFIP Conference, 31.8 - 4.9, NYC, 762–770.
# $\\[0.05in]$

# Werbos, P.J. (1988). Generalization of backpropagation with application to a recurrent gas market model. Neural networks, 1(4), 339-356.
# $\\[0.05in]$

# Werbos, P.J. (1990). Backpropagation through time: what does it do and how to do it. In Proceedings of IEEE, volume 78, 1550–1560.
# $\\[0.05in]$

# White, H. (1988). Economic prediction using neural networks: the case of IBM daily stock returns. IEEE 1988 International Conference on Neural Networks.
# $\\[0.05in]$

# Widrow, B. & Hoff, M. (1962). Associative storage and retrieval of digital information in networks of adaptive neurons. Biological Prototypes and Synthetic Systems, 1-160.
# $\\[0.05in]$

# Wilkinson, J. H., editor (1965). The Algebraic Eigenvalue Problem. Oxford University Press, Inc., New York, NY, USA.
# $\\[0.05in]$

# Williams, R. J. (1989). Complexity of exact gradient computation algorithms for recurrent neural networks. Technical Report Technical Report NU-CCS-89-27, Boston: Northeastern University, College of Computer Science.
# $\\[0.05in]$

# Willshaw, D. J. & von der Malsburg, C. (1976). How patterned neural connections can be set up by self-organization. Proc. R. Soc. London B, 194, 431–445.
# $\\[0.05in]$

# Xiong, R.X., Nichols, E.P. & Shen, Y. (2016). Deep learning stock volatility with Google domestic trends. arXiv:1512.04916v3.
# $\\[0.05in]$

# Yang, D. & Zhang, Q. (2000). Drift‐independent volatility estimation based on high, low, open, and close prices. The Journal of Business, 73(3),
# 477–492.
# $\\[0.05in]$

# Yu, R., Zheng, S. Anandkumar, A. & Yue, Y. (2019). Long-term forecasting using higher-order tensor RNNs. Journal of Machine Learning Research 1 (2019) 1-48.
# $\\[0.05in]$

# Yu, J., Yang, Z. & Zhang, X. (2006). A class of nonlinear stochastic volatility models and its implications for pricing currency options. Computational Statistics and Data Analysis, 51(4), 2218-2231.
# $\\[0.05in]$

# Zaheer, M., Ahmed, A. & Smola, A.J. (2017). Latent LSTM allocation: Joint clustering and non-linear dynamic modeling of sequence data. International Conference on Machine Learning, Sydney, Australia, PMLR 70.
# $\\[0.05in]$

# Zhang, P.G. & Min, Q. (2005). Neural network forecasting for seasonal and trend time series. European journal of operational research, 160(2), 501-514.
# $\\[0.05in]$

# Zheng, S., Yue, Y.S., & Lucey, P. (2016). Generating long-term trajectories using deep hierarchical networks. In Advances in Neural Information Processing Systems, 1543-1551.
# $\\[0.05in]$

# Zhu, L.X. & Laptev, N. (2017). Deep and confident prediction for time series at Uber. In Data Mining Workshops (ICDMW), 2017 IEEE International
# Conference, 103-110. IEEE, 2017.
# $\\[0.05in]$
