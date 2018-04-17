# binary_tree
To convert gene-presence-absence matrix into multi fasta alignment for tree building. This tool requires Python.

# Usage
Firstly download the Python scripts transpose.py and fasta.py in the working directory.

```
$ export PATH=$PATH:<working_directory>
```
Then the usage
```
$ cut -f2- testmatrix | transpose.py| fasta.py > output.fa   # output.fa can be any output filename
```

## Gene-presence-absence matrix
The gene-presence-absence matrix has to be something similar to the following:
```
    Genome1 Genome2 Genome3
pfo     1       1       1
apo     1       0       1
aab     0       0       1
por     1       0       0
plc     0       1       1
```
## Output
The generated output will be something like this:
```
>Genome1
11010
>Genome2
10001
>Genome3
11101
```
The multiple alignment will now be useful for tree building
