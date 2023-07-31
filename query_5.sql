SELECT sub.subject_id, sub.subject_name
FROM subjects sub
JOIN teachers t ON sub.teacher_id = t.teacher_id
WHERE t.name = 'Brandon Duncan';
