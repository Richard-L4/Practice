import os


# Set the secret keys only if they're not already set in the environment
os.environ.setdefault('STRIPE_SECRET_KEY', 'sk_test_51RSCyJQTwqMpoNnCxn386IWqceD9EuPz0mtI3yCucqVZjkLdY6A8jjAKsYb8MBIFRj3vzcFGhk9JmOc7LzLNDwOp00Sd72zH4F')
os.environ.setdefault('STRIPE_PUBLISHABLE_KEY', 'pk_test_51RSCyJQTwqMpoNnCWiXkpekCfh09B8X8RYYmPsnI6apyK0coYMA5p0lwpeWwZMf50ZLJWE8eCZO5GRcvK5VRczEv00TNEL7POT')
os.environ.setdefault('STRIPE_WH_SECRET', 'whsec_2aae94088b63ebdebb12eef5e8bfe6ed2568b88de81ed163926a021e2b2e9a01')
os.environ.setdefault("SECRET_KEY",  'django-insecure-bf_nx7m0sd(kbofoqv1g*ba))$ux)2(ju#mr-kr5#21@5iql_d')