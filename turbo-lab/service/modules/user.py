from flux import State, Mutation, register

state = State()
mutation = Mutation()

@register(state)
def user_rank(uid):
    return 0


@register(mutation)
def inc_rank(uid, rank):
    return rank+1