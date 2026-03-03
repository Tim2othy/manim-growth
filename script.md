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

### Solving for $y$

- I said at the start we care about GDP per capita, we get this by divding Y by L
- i call this $y$, I will always use lowercase letters for per capita terms, similarly k is K/L
- we want to know how $y$ changes, first we solve for $y$ at some point in time

$$
Y = K^\alpha L^{1-\alpha}
$$

$$
Y/L = \frac{K^\alpha}{L}   L^{1-\alpha}
$$

rewrite as

$$
Y/L = \frac{K^\alpha}{1}   L^{-\alpha}
$$

and

$$
Y/L = (\frac{K}{L})^\alpha 
$$

and so $y = k ^\alpha$

> show plot of this, one axsis is k other is y = k ^alpha

## Population

- Our second function is very simple
- population grows at a constant exponential rate
- $L(t) = L_0 e^{n t}$
- This is useful to use to analyse how we will look at growth in the long term.
- Just taking the derivative $\frac{\partial L}{\partial t} = \dot L$ which we call L dot as always is of course
- $\dot L = n L_0 e^{n t}$ but with constant growth like this it makes sense to look at the growth rate. clearly this is $n$ in this case but to derive this we:
- will use a method that is practical throught this topic, taking logs and then derivatives

$$ L_t = L_0 e^{n t} $$$$ \log( L_t) = \log(L_0 e^{n t} )  $$

$$ \log( L_t) = \log(L_0) + \log( e^{n t} )\ $$

$$ \log( L_t) = \log(L_0) + n t\ $$

and taking the derivative

$$
\frac{\dot L}{L}  = 0 + n = n\
$$

there are two things to understand here:
1. Understanding intuitivly why $\frac{\dot L}{L}$ is what we need:
	1. With exponential growth the added population is proportional to the current existing population so we want to know what this proportion is
	2. the added population is L_dot deviding this by the current population L returns us the answer
	3. this is also a useful way to define exponential growth, it's the only function where L_dot /L is a constant
2. Second is why taking logs and differentiating gives us this result, mathematically it's easy,
	1. diffing log L gives us L_dot / L
	2. but intuitivly understand that if you have ...

## Kapital transition function

- We turn to the second important equation.
Now time becomes important for the first time, just for simplicity I will explain the discrete version of this model for a moment, but will turn to the continuous version again afterwards.

- we have in one year K_n, what is the kapital next year, K_n+1?
- some amount of our capital deprecates, often 5%
- so we have $K_{n+1} = (1-\delta) K_n$
- clearly this would go to zero, so we also need to add kapital.
- The new kapital comes from investment
- $K_{n+1} = (1- \delta) K_n + S$
- S is the total amount. think of it as a fraction of output so S = s Y_n
- so we have $K_{n+1} = (1-\delta) K_n + s Y_n$
- going to the continous version first we solve for the change in kapital in the discrete version
- K_n+1 - K_n = s Y_n - delta K_n
- In the continuous version this simply becomes:
- $\dot K_t = s Y_t - \delta K_t$
- as everything is happening at the same time t we can leave the time subscrips out again: $\dot K = s Y - \delta K$
- with our cobb douglas production function this is
- $\dot K = s K^\alpha L^{1-\alpha} - \delta K$

### Transform into per capita version

start with $k = K/L$ take logs and get

$\log k = \log K - \log L$ and take the derivative to get:

$$\frac{\dot k}{k} = \frac{\dot K}{K} -  \frac{\dot L}{L}$$

we know the last part is n so can write

$$\frac{\dot k}{k} = \frac{\dot K}{K} -  n$$

substituting in our equation for K dot we get

$$\frac{\dot k}{k} = \frac{s Y - \delta K}{K} -  n$$

$$\frac{\dot k}{k} = s \frac{ Y}{K} -\delta -   n$$

and as

$$\frac{\dot k}{k} = s \frac{ y}{k} -\delta -   n$$

and multiplying by k

$$\dot k = s y - k( \delta +   n)$$

so change in kapital per person is determined by 3 terms two we have discussed already, deprication and saving, but now we also have population growth, the faster a population grows the more people we have to give kapital to, super fast growth means less kapital per person.
- this is made clear if population is shrinking, then clearly suddenly there is more kapital for each person alive

## Solving model

split into exogenous and endogenous values

exogenous parameters (singe values): $\delta, \alpha, s, n, k_0, L_0$

endogenous: what our model produces:
- time series of $Y, K, y, k$ are what interest us

### Solow diagram

Using essentially only our accumulation function.

$$\dot k = s y - k( \delta +   n)$$

the kapital lost and gained
- kapital gained is $sy = sk ^\alpha$

> create plot of that

and the lost kapital per person $-k( \delta +   n)$

> plot this also

we get this phase diagram that tells us where our economy will move next.
in the area with k higher than k* kapital will shrink
and below will grow
we have a stable equilibrium

## Example logs and diff

say we have our cobb douglas fun:

$$
Y= K^\alpha L^{1-\alpha}
$$

taking the log on both side

$$
\log Y = \log K^\alpha + \log L^{1-\alpha}
$$

of course is

$$
\log Y = \alpha \log K + (1-\alpha)\log L
$$

now taking the derivative on both sides, we relate the growth rate of output to the growth rate of Kapital and Labour

$$
\frac{\dot Y}{Y} = \alpha \frac{\dot K}{K} + (1-\alpha) \frac{\dot L}{L}
$$

we see that the growth rate of Output is a weighted average of the growth rate of Kapital and of Labour

## Analysis

- Now we have the 3 equations governing this economy
- and can look at what they imply for growth in our economy.

## Microfoundations

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
