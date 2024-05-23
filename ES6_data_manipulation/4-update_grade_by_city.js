export default function updateStudentGradeByCity(obj, city = '', newGrades) {
  if (!Array.isArray(obj) || !Array.isArray(newGrades)) {
    return [];
  }
  const studentByCity = obj.filter((student) => student.location === city).map((student) => {
    const grades = newGrades.filter((note) => student.id === note.studentId);
    let grade = 'N/A';

    if (grades[0]) {
      grade = grades[0].grade;
    }

    return { ...student, grade };
  });

  return studentByCity;
}
