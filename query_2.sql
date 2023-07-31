SELECT s.student_id, s.name, AVG(g.grade) as avg_grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects sub ON g.subject_id = sub.subject_id
WHERE sub.subject_name = 'Math'
GROUP BY s.student_id
ORDER BY avg_grade DESC
LIMIT 1;
