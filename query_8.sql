SELECT t.name, AVG(g.grade) as avg_grade
FROM teachers t
JOIN subjects sub ON t.teacher_id = sub.teacher_id
JOIN grades g ON sub.subject_id = g.subject_id
WHERE t.name = 'John Cisneros'
GROUP BY t.teacher_id;
