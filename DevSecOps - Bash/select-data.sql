SELECT to_user, text, created_at
FROM users u
  JOIN follows f
    ON u.username=f.from_user
  JOIN tweets t
    ON f.to_user=t.username
  WHERE u.username='_DreamLead'