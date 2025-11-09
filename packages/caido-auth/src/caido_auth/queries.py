"""GraphQL queries and mutations for Caido authentication."""

from gql import gql

START_AUTHENTICATION_FLOW = gql(
    """
    mutation StartAuthenticationFlow {
        startAuthenticationFlow {
            request {
                id
                userCode
                verificationUrl
                expiresAt
            }
            error {
                ... on AuthenticationUserError {
                    code
                    reason
                }
                ... on CloudUserError {
                    code
                    reason
                }
                ... on InternalUserError {
                    code
                    message
                }
                ... on OtherUserError {
                    code
                }
            }
        }
    }
    """
)

REFRESH_AUTHENTICATION_TOKEN = gql(
    """
    mutation RefreshAuthenticationToken($refreshToken: Token!) {
        refreshAuthenticationToken(refreshToken: $refreshToken) {
            token {
                accessToken
                expiresAt
                refreshToken
                scopes
            }
            error {
                ... on AuthenticationUserError {
                    code
                    reason
                }
                ... on CloudUserError {
                    code
                    reason
                }
                ... on InternalUserError {
                    code
                    message
                }
                ... on OtherUserError {
                    code
                }
            }
        }
    }
    """
)

CREATED_AUTHENTICATION_TOKEN_SUBSCRIPTION = gql(
    """
    subscription CreatedAuthenticationToken($requestId: ID!) {
        createdAuthenticationToken(requestId: $requestId) {
            token {
                accessToken
                expiresAt
                refreshToken
                scopes
            }
            error {
                ... on AuthenticationUserError {
                    code
                    reason
                }
                ... on InternalUserError {
                    code
                    message
                }
                ... on OtherUserError {
                    code
                }
            }
        }
    }
    """
)
