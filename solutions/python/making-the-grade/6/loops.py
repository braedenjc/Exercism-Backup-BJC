"""Functions for organizing and calculating student exam scores."""
import math
PASSING_GRADE_FLOOR = 41
FAILING_GRADE_CEILING = 40

def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    for score in student_scores:
        student_scores[student_scores.index(score)] = round(score)
    
    return student_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    count = 0
    for score in student_scores:
        if score <= 40:
            count += 1
    
    return count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    best_scores = []
    for score in student_scores:
        if score >= threshold:
            best_scores.append(score)
    
    return best_scores


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    grade_range = highest - FAILING_GRADE_CEILING
    grade_delta = math.floor(grade_range / 4)
    current_grade_threshold = PASSING_GRADE_FLOOR
    thresholds = [0, 0, 0, 0]
    for index, threshold in enumerate(thresholds):
        thresholds[index] = current_grade_threshold
        current_grade_threshold += grade_delta

    return thresholds


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    student_ranks = []
    for index, score in enumerate(student_scores):
        rank_string = f"{index+1}. {student_names[index]}: {score}" 
        student_ranks.append(rank_string)
        
    return student_ranks

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for student in student_info:
        if student[1] == 100:
            return student
            
    return []
