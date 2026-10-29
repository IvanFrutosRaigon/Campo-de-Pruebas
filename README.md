# Aprendizaje de programación

Mi hoja de ruta para aprender programación con foco en **criterio**: fundamentos, diseño de software y arquitectura de sistemas. Áreas: web, backend y datos.

- 📓 Diario de sesiones: [diario.md](diario.md)
- 📚 Apuntes: [apuntes/](apuntes/)
- 🧪 Ejercicios: [ejercicios/](ejercicios/)

> Ritmo orientativo: 8-10 horas semanales. Los tiempos son una guía, no un examen.

---

## Fase 0 · Base sólida en Python (2-3 meses)

- [x] Instalar Python y VS Code
- [x] Crear cuenta en GitHub y aprender lo básico de Git (`add`, `commit`, `push`, `pull`)
- [ ] Variables y tipos de datos
- [ ] Estructuras de control (`if`, `for`, `while`)
- [ ] Funciones
- [ ] Listas, tuplas, diccionarios y conjuntos
- [ ] Leer y escribir archivos
- [ ] Manejo de errores (`try` / `except`)
- [ ] Clases y objetos
- [ ] Módulos y paquetes, entornos virtuales (`venv`) y `pip`
- [ ] **Proyecto:** programa de consola útil (gestor de gastos o de tareas) que guarde los datos en un archivo

## Fase 1 · Cómo funcionan las cosas (1-2 meses, en paralelo)

- [ ] Uso básico de la terminal
- [ ] Cómo funciona la web: cliente-servidor, HTTP, DNS
- [ ] Estructuras de datos: arrays, listas enlazadas, pilas, colas, árboles, tablas hash
- [ ] Complejidad algorítmica (Big O) a nivel intuitivo
- [ ] Búsqueda y ordenación básicas
- [ ] Curso CS50 de Harvard (o al menos sus primeras semanas)

## Fase 2 · Bases de datos (1-2 meses)

- [ ] SQL: `SELECT`, `WHERE`, `ORDER BY`
- [ ] SQL: `JOIN`s
- [ ] SQL: agregaciones (`GROUP BY`, `COUNT`, `SUM`…)
- [ ] Modelado: tablas, relaciones, claves primarias y foráneas
- [ ] Normalización
- [ ] Índices y transacciones
- [ ] Practicar con SQLite y PostgreSQL
- [ ] **Proyecto:** rehacer el de la fase 0 guardando los datos en una base de datos bien diseñada

## Fase 3 · Web completa (3-4 meses)

**Backend**
- [ ] Framework de Python (FastAPI o Django)
- [ ] Diseño de APIs REST
- [ ] Validación de datos
- [ ] Autenticación y autorización

**Frontend**
- [ ] HTML
- [ ] CSS
- [ ] JavaScript
- [ ] TypeScript
- [ ] React

- [ ] **Proyecto:** aplicación web completa con usuarios, login y base de datos

## Fase 4 · Diseño de software (2-3 meses, y continuo)

- [ ] Principios SOLID
- [ ] Acoplamiento y cohesión, composición frente a herencia
- [ ] Patrones: Strategy, Factory, Observer, Adapter, Repository
- [ ] Testing con `pytest` (unitarios e integración)
- [ ] Código limpio y refactorización
- [ ] **Proyecto:** refactorizar la app de la fase 3 aplicando lo aprendido

Recursos: refactoring.guru · *Clean Code* · *Refactoring* (Martin Fowler)

## Fase 5 · Datos (2-3 meses)

- [ ] Pandas
- [ ] Visualización (matplotlib / seaborn)
- [ ] Estadística básica
- [ ] Pipelines de datos (ETL)
- [ ] (Opcional) Introducción a machine learning
- [ ] **Proyecto:** analizar un conjunto de datos público (datos.gob.es, Kaggle…) y sacar conclusiones

## Fase 6 · Llevarlo a producción (1-2 meses)

- [ ] Docker
- [ ] Despliegue en la nube
- [ ] CI/CD con GitHub Actions
- [ ] Seguridad básica (OWASP Top 10)
- [ ] Logs y monitorización
- [ ] **Proyecto:** desplegar la app web para que sea accesible desde internet

## Fase 7 · Arquitectura de sistemas (continuo)

- [ ] Arquitectura limpia / hexagonal
- [ ] Domain-Driven Design (DDD)
- [ ] Monolito vs. microservicios
- [ ] Arquitecturas orientadas a eventos y colas de mensajes
- [ ] Cachés y escalabilidad
- [ ] Consistencia vs. disponibilidad (teorema CAP)
- [ ] Documentar decisiones con ADRs (Architecture Decision Records)

Recursos: *Designing Data-Intensive Applications* (Martin Kleppmann) · repositorio *system-design-primer* en GitHub

---

## Proyectos

Cada proyecto vive en su propio repositorio. Enlázalos aquí al terminarlos:

| Fase | Proyecto | Repositorio |
|------|----------|-------------|
| 0 | Programa de consola | — |
| 2 | Versión con base de datos | — |
| 3 | Aplicación web | — |
| 5 | Análisis de datos | — |
| 6 | App desplegada | — |

## Reglas para trabajar con IA

1. Si no entiendo el código que me da, no lo uso hasta entenderlo.
2. Preguntar siempre: ¿por qué lo ha hecho así? ¿Qué alternativas había?
3. En la fase 0, escribo yo el código; la IA me explica.
4. Las decisiones de diseño las tomo yo.
