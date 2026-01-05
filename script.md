> Everything written with a > at the start is shown in the video

the other things might also be shown if I forgot to add an explicit instruction here,
some small things like a small arrow pointing somewhere I might forget

The Elegant theory of Economic growth

# Introduction

  - In this video I will explain the economic theory of long run economic growth.

> Show plot of long run growth, with some years shown, just use exponential function for now, y-axis is gdp per capita

  - Long run here means we are concerned with changes over multiple years, often around 10 - 100, there are also models going over thousans of years.
  - What causes us to be wealthier today than 30, 80, 200 years ago.
  - By wealth I always mean per capita wealth, and adjusting for inflation, basically how much can you buy.
  - Becoming more productive and so having to work less would also count here, productivity per hour is what matters

- We want to develop a model to understand why this is the case.
- There are two good ways to constrain our model
	1. All assumptions should be intuitivly plausible, and realistic
	2. It needs to explain the historic growth data we have
- Ill start with some intuitivly plausible assumptions
# Solow

## Production function

- I'll start with the most important part of the economy, the production function

> Show $Y_t$ then just $Y$ large on screen

- the amount of goods the economy produces at some point in time is $Y_t$ or just $Y$, I'll leave the subscript out if it won't cause confusion.
- And it uses some inputs for this.
	- For simplicity we just assume 2 inputs Labor and Capital
	- so total production is a function of them

> $Y = F(L, K)$

- L is just the number of people, K is some mesurment of all kapital
- in the stone age we might have 500 people with stones and tents
- and later a million with industrial machienes

> these assumptions are written out in the left of the screen in small font
> each time a new assumption is explained that is done in the center, once done it moves in line to the side

The following are assumptions we make about the production function:

### Assumption 1. continuity and differentiability
	- A tiny increase in any input leads to a tiny change in output
	- Maybe not 100% realistic but reasonable approximation

### Assumption 2. If we double everything the output is doubled

> $2Y = F(2 L, 2K)$

- The motivation is that if we imagine creating an exact copy of a factory or country, clearly the output is doubled.
- This is most obvious if we had one island with a factory and now create a second one far away

> one desert islands shown with a factory on it, for now just create a sand colored circle with a grey square on it, I'll later look into if I should import images somehow or so to do this. but the super simple shapes are enough for now
> Also show tiny stick figures next to the factory
> and above the output is 100 coconuts (use the emoji for this)
> then add add a second island next to the first one
> above it shifts to show 100 + 100 = 200 coconuts

- If they are close together there could be complications e.g. allowing for more specialisation more than doubles output, or coordination problems mean output is only increased by 80%, but for now we stick to this simple model
- Of course this doesn't only hold for 2 but for any lambda
> use lambda not 2 in equation

- We call this function homogenious of degree 1, or linearly homogenous
- In more economic terms we can say it exibits constant returns to scale.

### Ass 3. Positive and Diminishing Marginal Products,

- So we know what happens if we increase everything together, but what if just L or K is increased
> show derivative of F wrt. L and K

- We assume positive derivatives, more always increases production, but more interestingly diminishing marginal returns
- holding labour constant more Capital becomes less and less useful
 > plot this, show K on x axis and Y on other one, and just use normal cobb douglas function to generate the plot.
 > then wait couple of seconds and add tangent line, first at very left where derivative is super high, then the tangent line moves along the graph to the right and we see it become almost flat

- the motivation is simple, in some factory with 50 workers and 20 machines probably adding an 21st is useful, but each one becomes less so, until at 50 machiens per worker the benefit is tiny
- the same applies other way around


### Cobb douglas

Instead of working with maximal generallity we assume a specific form cobb douglas

> $F(L, K) = K^\alpha L^{1-\alpha}$


- You can check that all assumptions are satisfied


### Firms problem


- We can imagine the economy being made up of many firms maximising their profit, their profit is
- price * production - payments

> max_{} K, L} F(K, L)-rK-wL.

- we can set the price to 1
- And expendeture is wage * number of emploees
- and rental price of kapital * Amount of kapital
- taking derivatives ...
- and we get
- wL+rK=Y
- so the firms make no profits, wages and rents eat up all production

### Eulers theorem

- Actually true for all linearly homogenous functions
$$
g(L,K)=g_L(L,K)L + g_K(L,K)K
$$
the derivatives times the amont equal the output

## Kapital acumulation function

- We turn to the second important equation.
Now time becomes important for the first time, just for simplicity I will explain the discrete version of this model for a moment, but will turn to the continuous version again afterwards.

- we have in one year K_n, what is the kapital next year, K_n+1?
- some amount of our capital deprecates, often 5%
- so we have K_n+1 = (1-delta) K_n
- clearly this would go to zero, so we also need to add kapital.
- The new kapital comes from investment
-  K_n+1 = (1-delta) K_n + S
-  S is the total amount. think of it as a fraction of output so S = s Y_n
-  so we have K_n+1 = (1-delta) K_n + s Y_n

- going to the continous version first we solve for the change in kapital in the discrete version
- K_n+1 - K_n = s Y_n - delta K_n
- In the continuous version this simply becomes:
- K_dot_t = s Y_t - delta K_t
- as everything is happening at the same time t we can leave the time subscrips out again.
- with our cobb douglas production function this is
- K_dot_t = s K_t^alpha L_t^(1-alpha) - delta K_t
