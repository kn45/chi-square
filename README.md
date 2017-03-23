# Chi-Squared Test
This project provide a text feature selection method with chi-squared test.  
The script could run in stand-alone mode or cluster mode by hadoop streaming.  
https://github.com/kn45/Chi-Square
***
| \---         | cat   | non-cat | sum over cats |
| ------------ | ----- | ------- | ------------- |
| with word    | A[]   | B[]     | A+B           |
| without word | C[]   | D[]     | C+D           |
| sum          | A+C[] | B+D[]   | N             |
***
$\chi^2 = \frac{N(AD-BC)^2}{(A+C)(A+B)(B+D)(C+D)}$  
$\chi^2 = \frac{(AD-BC)^2}{(A+B)(C+D)}$ (abbrev for in-cat scenario)
## Input Format
cat`[TAB]`segments  
cat is class label in string while segments are space separeted words from a certain passage  
eg:  
sport`[TAB]`well done MSN congrats to Barcelona  

## Output Format

cat`[TAB]`word`[TAB]`chi2_value`[TAB]`A`[TAB]`B`[TAB]`C`[TAB]`D`[TAB]`pos  
pos means positive(1) or negative(-1) relative  
## Dict Format

A file records the pre-computed number of passages of each category with format:  
cat`[TAB]`count  
e.g.:   
fashion`[TAB]`347882  
sport`[TAB]`2443297   

## Usage

#### stand-alone:

`cat input_passage.tst | ./mapred_chi2.py m | sort | ./mapred_chi2.py r passage_cnt_file > output_chi2.tst`
####cluster:
Refer to run_chi2_uni.sh
