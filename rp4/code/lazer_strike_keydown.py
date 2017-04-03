if color.type == pygame.KEYDOWN:
  if color.key == pygame.K_w:
    pygame.draw.line(
        screen,
        red,
        start_pos,
        end_pos,
        3
    )
    ...
