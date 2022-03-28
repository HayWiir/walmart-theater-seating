## Task

  

Create an application that allows users to search over the top wikipedia pages as defined by

[this wikipedia article](https://en.wikipedia.org/wiki/Wikipedia:Multiyear_ranking_of_most_viewed_pages).

The application should provide an API that allows users to submit a request with a free text query and receive

back an array of results containing the documents that were relevant to the input query. The documents will be limited

to the following lists which appear in the above article:

  

- Top-100 list

- Countries

- Cities

- Buildings & Structures & Statues

- People

- Singers

- Actors

- Romantic Actors

- Athletes

- Modern political leaders

- Pre-modern people

- 3rd-millennium people

  

### Provided

  

This repo provides a utility to load the data from those articles into an elasticsearch index called `wikis`.

Running the following command will bring up an elasticsearch instance as well as a utility which will load the

above data into that elasticsearch instance.

  

```

docker-compose up

```

  

In order to keep the assignment consistent and not subject to

wikipedia being a static asset, the program doesn't actually reach out to the wiki page. Instead, it loads the `wikis` index from a local snapshot.

  

### Movie Theater Seating - Walmart

A service for assigning seats within a movie theater to
fulfill reservation requests.

Logic:
- Maintain a preference of rows (middle rows have higher preference)
- Assign seating in preferred rows from left to right
- Earliest requests assigned first.
- All seats are together if possible. Even if seats have to be split, the split groups are assigned together. (Preferred row seating has higher preference over Together seating)
 
There are 3 files:
- `theater.py`: Contains theater class and methods that implement the algorithm as well as helper functions.
- `main.py`: Entry file for execution that reads and processes input and writes output.
- `test.py`: Unit test file. Can be executed using pytest.

Input Format:
- Input is read from an `input.txt` file placed in root of repo directory.
- There can be multiple requests in each file. Eac request on a newline.
- Requests are of the format {Request ID} {Number of Tickets requested}. For e.g. `R001 4`

Output Format:
- Output is written to `output.txt` created in the root of repo directory.
- Output is of the format {Request ID} {Reserved Tickets}. For e.g. `R001 F1,F2,F3,F4`

How to run: 
- General Execution: `python3 main.py` (Make sure `input.txt` exists)
- Tests: `python3 -m pytest test.py`