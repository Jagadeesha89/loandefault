from loandefault.entity.artifactentity import ClassificationMetricArtifact
from loandefault.exception.exception import LoandefaultException
from sklearn.metrics import f1_score,accuracy_score,precision_score,recall_score
import sys

def get_classification_score(y_true,y_pred):
    try:
        model_f1_score=f1_score(y_true,y_pred)
        model_recall_score=recall_score(y_true,y_pred)
        model_precision_score=precision_score(y_true,y_pred)
        model_accuracy_score=accuracy_score(y_true,y_pred)

        classification_mertic = ClassificationMetricArtifact(f1_score=model_f1_score,
                                                            precision_score=model_precision_score,
                                                            recall_score=model_recall_score,
                                                            accuracy_score=model_accuracy_score)
        
        return classification_mertic
    except Exception as e:
        raise LoandefaultException(e,sys)
