interface Option {
  label: string;
  value: number;
}

export interface QuestionType {
  id: number;
  title: string;
  description: string;
  type: 'one-of-list' | 'some-of-list' | 'text' | 'scale' | 'grade';
  options: {
    variants?: Option[];
  };
}
