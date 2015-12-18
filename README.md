This is collected code from our final project for CSE 544. Our random forests implementation does not function with the current Myria system, as it does not support nested do/while loops. However, we hope this serves as a valuable resource, regardless. For more, see our report, in final_report.pdf.

Our main code is stored across three files:
1. denorm.myl (reads in csvs from uw hosting (mirrored locally) into the database)
1. trainer.myl (trains a number of trees from the denormalized data)
1. tester.myl (tests data in the test set against the trees)