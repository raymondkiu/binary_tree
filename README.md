# binary_tree
To convert gene-presence-absence matrix into nucleotide-based multi fasta alignment for tree building. This tool requires Python module.

# Usage
Firstly download the Python scripts transpose.py and fasta.py in the working directory.

```
$ export PATH=$PATH:<working_directory>
```
Then the usage
```
$ cut -f2- new-gene-presence-absence-matrix | transpose.py| fasta.py > output.fa   # output.fa can be any output filename
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

To replace 1 with C and 0 with A for tree building as they usually do not recognise 1 and 0 (e.g. Fasttree), use sed command for text processing:

```
sed 's/\t/,/g' gene-presence-absence-matrix |sed 's/,1/,C/g;s/,0/,A/g'|sed 's/,/\t/g' > new-gene-presence-absence-matrix 
```

Now it should look something like this:
```
    Genome1 Genome2 Genome3
pfo     C       C       C
apo     C       A       C
aab     A       A       C
por     C       A       A
plc     A       C       C
```
The matrix is now ready for the usage in the above section

## Output
The generated output will be something like this:
```
>Genome1
CCACA
>Genome2
CAAAC
>Genome3
CCCAC
```
This multiple alignment will now be useful for tree building.
