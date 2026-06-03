# Action facts

#### Start(tid, identity, name)
Used in restriction `one_role_per_actor` to ensure one role per actor.
* **tid**: Identifier of the session
* **actor**: Public identity of the actor
* **role**: String representing the actors role

#### Neq(a, b)
Used in restriction `neq_check` to ensure two variables are not equal.
* **a**: Variable a
* **b**: Variable b