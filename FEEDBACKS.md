## Some thoughts

- Not sure where to write domain logic , either in use cases or in the entity itself ?
- seems a lot of extra code to be written when following hexagonal principles.
- Should I inject the use case into the API route handler? I usually inject external dependencies that I might want to fake in tests, such as repositories or external clients. That's not the case for use cases, since they contain the domain logic I actually want to test and keep. As a result, I don't unit test API route handlers directly.