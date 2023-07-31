SELECT g.group_id, AVG(gr.grade) as avg_grade
FROM groups g
JOIN students s ON g.group_id = s.group_id
JOIN grades gr ON s.student_id = gr.student_id
JOIN subjects sub ON gr.subject_id = sub.subject_id
WHERE sub.subject_name = 'Mechatronics'
GROUP BY g.group_id;