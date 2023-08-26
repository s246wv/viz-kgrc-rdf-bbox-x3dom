# viz-kgrc-rdf-bbox-x3dom

## Usage

### Premise
- GraphDB
  - This notebook is intended to use [GraphDB](https://graphdb.ontotext.com/) provided by OntoText. 
  - You need to get it and run the database server in your environment.  
  - The repository name should be `KGRC4SI_20230714_r2`. You can change this at the third cell in the notebook. 
- Knowledge Graph
  - You need to get the knowledge graphs for "Knowledge Graph Reasoning Challenge for Social Issue".
  - Please see [this repository](https://github.com/KnowledgeGraphJapan/KGRC-RDF/tree/kgrc4si) for detail.
- Python with the following packages
  - rdflib
  - sparqlwrapper

### Settings and run
1. Please input the required information to `graphdb_auth.txt`.
   1. The first line denotes the endpoint of your GraphDB environment.
   2. The second and the third lines denote your credential information.
2. Run notebook and then you will get the html files.
3. After open the html file, you can get 3D visualization of the specific scene.

## Acknowledgement
I would like to thank @YE-WIN-Unity for creating great notebook.  
I am also grateful to the great project "Knowledge Graph Reasoning Challenge for Social Issue". This repository is intended to use [the dataset](https://github.com/KnowledgeGraphJapan/KGRC-RDF/tree/kgrc4si) from the project.  
The visualization part is implemented by using [x3dom tech](https://www.x3dom.org/). I also thank the great project.  
