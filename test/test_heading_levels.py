from migcon.heading_info import HeadingInfo
from pathlib import Path

def test_heading_levels_case3():
    test_string = """
# Heading 1
### Heading 2
##### Heading 3
# Heading 4
### Heading 5
# Heading 6
# Heading 7
### Heading 8
##### Heading 9
####### Heading 10
### Heading 11
"""
    expected_results = """
# Heading 1
## Heading 2
### Heading 3
## Heading 4
### Heading 5
## Heading 6
## Heading 7
### Heading 8
#### Heading 9
##### Heading 10
### Heading 11
"""
    assert HeadingInfo.reconcile_heading_levels_in_file(test_string, Path("test")) == expected_results

def test_heading_levels_case2():
    test_string = """
# Heading 1
### Heading 2
##### Heading 3
### Heading 4
##### Heading 5
### Heading 6
### Heading 7
##### Heading 8
####### Heading 9
######### Heading 10
##### Heading 11
"""
    expected_results = """
# Heading 1
## Heading 2
### Heading 3
## Heading 4
### Heading 5
## Heading 6
## Heading 7
### Heading 8
#### Heading 9
##### Heading 10
### Heading 11
"""
    results = HeadingInfo.reconcile_heading_levels_in_file(test_string, Path("test"))
    assert results == expected_results

