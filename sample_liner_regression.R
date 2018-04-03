x <- rnorm(100)
y <- 2 + 3 * x + rnorm(100) * 0.5
str(x)
str(y)

model1 <- lm(y ~ x)
## print(summary(model1))

plot(x, y, main = "Sample linear regression")
abline(model1$coefficients, col = "blue")