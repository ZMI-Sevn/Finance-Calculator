# Finance Calculator
## Project produced during CoGrammar bootcamp
The scenario for this project:
  A small financial company has approached you with a request to create a program that allows users to access two different
  financial calculators: an investment calculator and a home loan repayment calculator.

## Formulas

Interest formula:
  The total amount when **simple interest** is applied is calculated as follows: 𝐴 = 𝑃*(1 + 𝑟 * 𝑡)
  The Python equivalent is very similar: A = P *(1 + r*t)
  The total amount when **compound interest** is applied is calculated as follows: 𝐴 = 𝑃*(1 + 𝑟)𝑡)
  
  The Python equivalent is slightly different: A = P * math.pow((1+r),t)
  In the formulae above:
    ● ‘r’ is the interest entered above divided by 100, e.g. if 8% is entered, then r is 0.08.
    ● ‘P’ is the amount that the user deposits.
    ● ‘t’ is the number of years that the money is being invested.
    ● ‘A’ is the total amount once the interest has been applied.

Bond repayment formula:
  The amount that a person will have to be repaid on a home loan each month is calculated as follows: 𝑟𝑒𝑝𝑎𝑦𝑚𝑒𝑛𝑡 =
  𝑖 × 𝑃/1 − (1+𝑖) −𝑛

  The Python equivalent is slightly different: repayment = (i * P)/(1 - (1 + i)**(-n))
  In the formula above:
    ● ‘P’ is the present value of the house.
    ● ‘i’ is the monthly interest rate, calculated by dividing the annual interest rate by 12. Remember to divide the interest
      entered by the user by 100 e.g. (8 / 100) before dividing by 12.
    ● ‘n’ is the number of months over which the bond will be repaid.
