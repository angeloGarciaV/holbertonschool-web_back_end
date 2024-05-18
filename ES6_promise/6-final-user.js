export default function handleProfileSignup(firstName = '', lastName = '', fileName = '') {
  return Promise.allSettled([uploadPhoto(fileName), signUpUser(firstName, lastName)])
    .then((results) => {
      return results.map((result, index) => {
        if (index === 0) {
          return { status: result.status, value: 'error' };
        } else {
          return { status: result.status, value: 'user' };
        }
      });
    });
}
